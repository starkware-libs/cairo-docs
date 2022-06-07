from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementFor,
    CodeElement,
    CodeElementAllocLocals,
)
from starkware.cairo.lang.compiler.ast.visitor import Visitor
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError


def lint_for_loop(elm: CodeElementFor):
    linter = _ForLoopLinter()
    linter.visit(elm.code_block)


class _ForLoopLinter(Visitor):
    def _visit_default(self, obj):
        assert isinstance(obj, CodeElement)

    # Override default implementations for AST nodes we do not want to go into.
    def visit_CodeElementFor(self, elm: CodeElementFor):
        pass

    def visit_CairoModule(self, module):
        pass

    def visit_CodeElementFunction(self, elm):
        pass

    def visit_CodeElementAllocLocals(self, elm: CodeElementAllocLocals):
        raise ForLoopLoweringError(
            "alloc_locals is not allowed in the body of a for loop.",
            location=elm.location,
        )
