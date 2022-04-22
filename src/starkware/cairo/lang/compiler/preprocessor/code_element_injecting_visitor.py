import dataclasses
from abc import ABC
from collections.abc import Iterable

from starkware.cairo.lang.compiler.ast.code_elements import (
    CommentedCodeElement,
    CodeBlock,
    CodeElementFunction,
)
from starkware.cairo.lang.compiler.ast.module import CairoModule
from starkware.cairo.lang.compiler.ast.visitor import Visitor


class CodeElementInjectingVisitor(ABC, Visitor):
    """
    Extension of Visitor interface which allows to:

    * Return many code elements from visitor methods when processing code elements inside a
      ``CodeBlock``.

    * Add new functions to generated Cairo code, by calling ``inject_function`` inside visitor
      methods. This visitor will try to put these new functions as close as possible to source
      code location, that is: in current ``CairoModule``, right after currently processed
      ``CodeElementFunction``.

    For example usage check out ``ForLoopLoweringVisitor.visit_CodeElementFor``.
    """

    def __init__(self):
        super().__init__()
        self._inject_functions = []

    def inject_function(self, func: CodeElementFunction):
        """
        Call from visitor method to register a new function to be added to current Cairo module
        as close as possible to source code location where this visitor has been called.
        """

        assert isinstance(func, CodeElementFunction)
        self._inject_functions.append(func)

    def visit_CodeBlock(self, elm: CodeBlock):
        can_inject_functions = isinstance(self.parents[-1], CairoModule)

        code_elements = []
        for commented_code_elm in elm.code_elements:
            visited_elm = self.visit(commented_code_elm.code_elm)

            # Flatten lists of code elements if returned from visitor method.
            if isinstance(visited_elm, Iterable):
                # This line forgets the comment assigned to commented_code_elm.
                # This shouldn't matter in current use cases, but please be aware of this.
                visited_elm = CodeBlock.from_code_elements(visited_elm).code_elements
            else:
                visited_elm = [dataclasses.replace(commented_code_elm, code_elm=visited_elm)]

            code_elements.extend(visited_elm)

            # Inject any new functions if possible.
            if can_inject_functions:
                for func in self._inject_functions:
                    assert isinstance(func, CodeElementFunction)
                    code_elements.append(
                        CommentedCodeElement(
                            code_elm=func,
                            comment=None,
                            location=getattr(elm, "location", None),
                        )
                    )

                self._inject_functions.clear()

        return dataclasses.replace(elm, code_elements=code_elements)
