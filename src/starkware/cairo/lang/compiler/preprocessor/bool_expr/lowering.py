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
        if isinstance(elm.condition, BoolEqExpr):
            return elm

        assert isinstance(elm.condition, BoolAndExpr)

        # TODO(mkaput, 19/05/2022): Support else blocks
        if elm.else_code_block is not None:
            raise BoolExprLoweringError(
                "Else blocks are not supported with boolean logic expressions yet.",
                location=elm.location,
            )

        # TODO(mkaput, 19/05/2022): Support more complex chains.
        if not isinstance(elm.condition.a, BoolEqExpr):
            raise BoolExprLoweringError(
                "Nested and expressions are not supported yet.", location=elm.condition.a.location
            )

        # Substitute:
        #
        #     if a and b:
        #         main_code_block
        #     end
        #
        # with:
        #
        #     if a:
        #         if b:
        #             main_code_block
        #         end
        #     end
        return CodeElementIf(
            condition=elm.condition.a,
            main_code_block=CodeBlock.singleton(
                CodeElementIf(
                    condition=elm.condition.b,
                    main_code_block=elm.main_code_block,
                    else_code_block=None,
                    location=elm.location,
                )
            ),
            else_code_block=None,
            location=elm.location,
        )
