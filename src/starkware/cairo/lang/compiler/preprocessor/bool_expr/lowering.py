import dataclasses

from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr, BoolAndExpr, BoolEqExpr
from starkware.cairo.lang.compiler.ast.code_elements import CodeElementIf, CodeBlock
from starkware.cairo.lang.compiler.ast.visitor import Visitor
from starkware.cairo.lang.compiler.preprocessor.bool_expr.errors import BoolExprLoweringError
from starkware.cairo.lang.compiler.preprocessor.pass_manager import VisitorStage, PassManagerContext


class BoolExprLoweringStage(VisitorStage):
    """
    Lowers boolean logic expressions in if conditions to nested if statements.

    This stage is relatively high level and should be placed early in the compilation pass chain.
    """

    def __init__(self):
        super().__init__(visitor_factory=BoolExprLoweringVisitor, modify_ast=True)


class BoolExprLoweringVisitor(Visitor):
    def __init__(self, context: PassManagerContext):
        super().__init__()
        self.context = context

    def _visit_default(self, elm):
        return elm

    def visit_CodeElementIf(self, elm: CodeElementIf) -> CodeElementIf:
        return ConditionLowering(elm).visit(elm.condition)


class ConditionLowering(Visitor):
    def __init__(self, source_elm: CodeElementIf):
        super().__init__()
        self.source_elm = source_elm

    def _visit_default(self, obj):
        assert isinstance(obj, BoolExpr)
        return obj

    def visit_BoolEqExpr(self, condition: BoolEqExpr) -> CodeElementIf:
        return dataclasses.replace(self.source_elm, condition=condition)

    def visit_BoolAndExpr(self, condition: BoolAndExpr) -> CodeElementIf:
        # TODO(mkaput, 19/05/2022): Support else blocks
        if self.source_elm.else_code_block is not None:
            raise BoolExprLoweringError(
                "Else blocks are not supported with boolean logic expressions yet.",
                location=self.source_elm.location,
            )

        # TODO(mkaput, 19/05/2022): Support more complex chains.
        if not isinstance(condition.a, BoolEqExpr):
            raise BoolExprLoweringError(
                "Nested and expressions are not supported yet.", location=condition.a.location
            )

        elm = self.visit(condition.b)
        return dataclasses.replace(
            self.source_elm,
            condition=condition.a,
            main_code_block=CodeBlock.singleton(elm),
            else_code_block=None,
        )
