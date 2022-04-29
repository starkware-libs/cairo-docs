import dataclasses
from abc import ABC
from contextlib import contextmanager
from typing import List, Iterable

from starkware.cairo.lang.compiler.ast.code_elements import (
    CommentedCodeElement,
    CodeBlock,
    CodeElementFunction,
)
from starkware.cairo.lang.compiler.ast.module import CairoModule
from starkware.cairo.lang.compiler.ast.visitor import Visitor


@dataclasses.dataclass
class CodeElementsInjection:
    code_elements: Iterable[CommentedCodeElement]

    @classmethod
    def from_code_block(cls, code_block: CodeBlock) -> "CodeElementsInjection":
        return cls(code_block.code_elements)


class CodeElementInjectingVisitor(ABC, Visitor):
    """
    Extension of Visitor interface which allows to:

    * Return many code elements from visitor methods when processing code elements inside a
      ``CodeBlock``. For this, return ``CodeElementsInjection``.

    * Add new functions to generated Cairo code, by calling ``inject_function`` inside visitor
      methods. This visitor will try to put these new functions as close as possible to source
      code location, that is: in current ``CairoModule``, right after currently processed
      ``CodeElementFunction``.

    For example usage check out ``ForLoopLoweringVisitor.visit_CodeElementFor``.
    """

    _injection_scopes: List[List[CodeElementFunction]]

    def __init__(self):
        super().__init__()
        self._injection_scopes = []

    def inject_function(self, func: CodeElementFunction):
        """
        Call from visitor method to register a new function to be added to current Cairo module
        as close as possible to source code location where this visitor has been called.
        """
        self._injection_scopes[-1].append(func)

    def visit_CairoModule(self, module: CairoModule):
        with self._injection_scope():
            return super().visit_CairoModule(module)

    def visit_CodeBlock(self, elm: CodeBlock):
        can_inject_functions = isinstance(self.parents[-1], CairoModule)

        code_elements = []
        for commented_code_elm in elm.code_elements:
            visited_elms = self.visit(commented_code_elm.code_elm)

            # Flatten lists of code elements if returned from visitor method.
            if isinstance(visited_elms, CodeElementsInjection):
                # This line forgets the comment assigned to commented_code_elm.
                # This shouldn't matter in current use cases, but please be aware of this.
                code_elements.extend(visited_elms.code_elements)
            else:
                code_elements.append(dataclasses.replace(commented_code_elm, code_elm=visited_elms))

            # Inject any new functions if possible.
            if can_inject_functions:
                current_injection_scope = self._injection_scopes[-1]

                for func in current_injection_scope:
                    code_elements.append(
                        CommentedCodeElement(
                            code_elm=func,
                            comment=None,
                            location=getattr(elm, "location", None),
                        )
                    )

                current_injection_scope.clear()

        return dataclasses.replace(elm, code_elements=code_elements)

    @contextmanager
    def _injection_scope(self):
        self._injection_scopes.append([])
        try:
            yield
        finally:
            injected_functions = self._injection_scopes.pop()
            assert not injected_functions, "There are leftover not injected functions!"
