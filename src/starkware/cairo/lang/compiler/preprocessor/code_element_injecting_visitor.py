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
class CodeElementInjection:
    """
    A list of code elements to be injected.
    """

    code_elements: Iterable[CommentedCodeElement]

    @classmethod
    def from_code_block(cls, code_block: CodeBlock) -> "CodeElementInjection":
        return cls(code_block.code_elements)


class CodeElementInjectingVisitor(ABC, Visitor):
    """
    Extension of Visitor interface which allows to:

    * Return many code elements from visitor methods when processing code elements inside a
      ``CodeBlock``. For this, return ``CodeElementsInjection``.

    * Add new functions to generated Cairo code, by calling ``inject_function`` inside visitor
      methods. This visitor will try to put these new functions as close as possible to source
      code location, that is: in the current ``CairoModule``, right after the currently processed
      ``CodeElementFunction``.

    For example usage check out ``ForLoopLoweringVisitor.visit_CodeElementFor``.
    """

    def __init__(self):
        super().__init__()

        # An injection scope is a list of functions to be added to the AST upon finishing visiting
        # a Cairo module or any other meaningful elements.
        #
        # We support nested Cairo modules here, so we store injection scopes in a stack.
        self._injection_scopes: List[List[CodeElementFunction]] = []

    def inject_function(self, func: CodeElementFunction):
        """
        Registers a new function to be added to the current Cairo module.

        The function will be added as close as possible to the source code location where this
        visitor has been called.

        This method can only be called from within other visitor methods.
        """
        self._injection_scopes[-1].append(func)

    def visit_CairoModule(self, module: CairoModule):
        with self._injection_scope():
            return super().visit_CairoModule(module)

    def visit_CodeBlock(self, elm: CodeBlock):
        can_inject_functions = isinstance(self.parents[-1], CairoModule)

        code_elements = []
        for commented_code_elm in elm.code_elements:
            visited_elm = self.visit(commented_code_elm.code_elm)

            # Flatten lists of code elements if returned from visitor method.
            if isinstance(visited_elm, CodeElementInjection):
                # Note that the following line ignores the comment assigned to commented_code_elm.
                code_elements.extend(visited_elm.code_elements)
            else:
                code_elements.append(dataclasses.replace(commented_code_elm, code_elm=visited_elm))

            # Inject any new functions if possible.
            if can_inject_functions:
                current_injection_scope = self._injection_scopes[-1]

                for func in current_injection_scope:
                    visited_func = self.visit(func)
                    code_elements.append(CommentedCodeElement(code_elm=visited_func, comment=None))

                current_injection_scope.clear()

        return dataclasses.replace(elm, code_elements=code_elements)

    @contextmanager
    def _injection_scope(self):
        self._injection_scopes.append([])
        try:
            yield
        finally:
            injected_functions = self._injection_scopes.pop()
            assert len(injected_functions) == 0, "Function injection failed to run completely."
