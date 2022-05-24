from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
)

from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFor
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManagerContext, VisitorStage


class ForLoopLoweringStage(VisitorStage):
    """
    Lowers for loops into calls to recursive functions.

    This stage is relatively high level and should be placed early in the compilation pass chain.
    """

    def __init__(self):
        super().__init__(visitor_factory=ForLoopLoweringVisitor, modify_ast=True)


class ForLoopLoweringVisitor(CodeElementInjectingVisitor):
    def __init__(self, context: PassManagerContext):
        super().__init__()
        self.context = context

    def _visit_default(self, elm):
        return elm

    def visit_CodeElementFor(self, elm: CodeElementFor):
        raise NotImplemented
