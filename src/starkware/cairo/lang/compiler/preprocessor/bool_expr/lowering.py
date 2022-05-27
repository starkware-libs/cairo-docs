from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr, BoolAndExpr, BoolEqExpr
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementIf,
    CodeBlock,
    CodeElementLabel,
    CodeElementInstruction,
)
from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier
from starkware.cairo.lang.compiler.ast.instructions import (
    InstructionAst,
    JumpToLabelInstruction,
)
from starkware.cairo.lang.compiler.ast.visitor import Visitor
from starkware.cairo.lang.compiler.preprocessor.pass_manager import VisitorStage, PassManagerContext
from starkware.cairo.lang.compiler.unique_name_provider import UniqueNameKind


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

        if elm.else_code_block is not None:
            label = ExprIdentifier(
                name=self.context.unique_names.next(UniqueNameKind.Label), location=elm.location
            )
            real_else_code_block = (
                CodeBlock.singleton(CodeElementLabel(identifier=label)) + elm.else_code_block
            )
            jump_to_else_code_block = CodeBlock.singleton(
                CodeElementInstruction(
                    InstructionAst(
                        body=JumpToLabelInstruction(
                            label=label, condition=None, location=elm.location
                        ),
                        inc_ap=False,
                        location=elm.location,
                    )
                )
            )
        else:
            real_else_code_block = None
            jump_to_else_code_block = None

        def lower_conjunction_chain(
            lhs: BoolExpr, main_code_block: CodeBlock, else_code_block: CodeBlock
        ) -> CodeElementIf:
            """
            Substitutes::

                if a and b:
                    main_code_block
                end

            with::

                if a:
                    if b:
                        main_code_block
                    end
                end

            Recursively for whole `and` chains.

            Python's recursion limit guards against getting into infinite loops, which may happen if
            the compiler has a bug and makes a loop in conditions tree.
            """
            if isinstance(lhs, BoolEqExpr):
                # We have reached innermost/first equation to check.
                return CodeElementIf(
                    condition=lhs,
                    main_code_block=main_code_block,
                    else_code_block=else_code_block,
                    location=elm.location,
                )

            assert isinstance(lhs, BoolAndExpr)

            return lower_conjunction_chain(
                lhs=lhs.a,
                main_code_block=CodeBlock.singleton(
                    CodeElementIf(
                        condition=lhs.b,
                        main_code_block=main_code_block,
                        else_code_block=else_code_block,
                        location=elm.location,
                    )
                ),
                else_code_block=jump_to_else_code_block,
            )

        return lower_conjunction_chain(elm.condition, elm.main_code_block, real_else_code_block)
