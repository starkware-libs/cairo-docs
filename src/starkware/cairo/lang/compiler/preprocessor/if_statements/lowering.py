import dataclasses
from typing import Dict

from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeBlock,
    CodeElementIf,
    CodeElementLabel,
    CodeElementConditionalJump,
    CodeElementEraseIfUnreachable,
)
from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ExprOperator
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
    CodeElementInjection,
)
from starkware.cairo.lang.compiler.preprocessor.if_statements.jumps import (
    Exit,
    JumpToLabelDescriptor,
    Terminal,
    convert_bool_expr_to_jumps,
    BoolExprId,
)
from starkware.cairo.lang.compiler.preprocessor.pass_manager import VisitorStage, PassManagerContext
from starkware.cairo.lang.compiler.unique_name_provider import UniqueNameKind


# TODO(mkaput, 02/06/2022): Port AuxiliaryInfoCollector support, or remove start/end if callbacks.


class IfLoweringStage(VisitorStage):
    """
    Lowers if statements to sequences of conditional jumps.

    This stage is relatively high level and should be placed early in the compilation pass chain.
    """

    def __init__(self):
        super().__init__(visitor_factory=IfLoweringVisitor, modify_ast=True)


class IfLoweringVisitor(CodeElementInjectingVisitor):
    def __init__(self, context: PassManagerContext):
        super().__init__()
        self.context = context

    def _visit_default(self, elm):
        return elm

    def visit_CodeElementIf(self, elm: CodeElementIf) -> CodeElementInjection:
        jump_table = convert_bool_expr_to_jumps(
            expr=elm.condition,
            has_false_case=elm.else_code_block is not None,
        )

        labels = {
            k: self.context.unique_names.next(UniqueNameKind.Label)
            for k in jump_table.reachable_items_ids()
        }

        assert (
            list(jump_table.keys())[0] not in labels.keys()
        ), "First jump must not need a label generated in order to enable attaching a hint to it."

        # Visit into if's code blocks.
        elm = dataclasses.replace(
            elm,
            main_code_block=self.visit(elm.main_code_block),
            else_code_block=self.visit(elm.else_code_block),
        )

        code_block = CodeBlock.empty()

        for key, item in jump_table.items():
            if key in labels:
                code_block += CodeBlock.singleton(
                    CodeElementLabel(
                        identifier=ExprIdentifier(name=labels[key], location=elm.location)
                    )
                )

            if isinstance(item, JumpToLabelDescriptor):
                code_block = _lower_jump_to_label_descriptor(
                    code_block=code_block, descriptor=item, labels=labels
                )
            elif isinstance(item, Terminal):
                code_block = _lower_terminal(
                    code_block=code_block,
                    terminal=item,
                    elm=elm,
                    labels=labels,
                )
            else:
                assert isinstance(item, Exit)

        return CodeElementInjection.from_code_block(code_block)


def _lower_jump_to_label_descriptor(
    code_block: CodeBlock,
    descriptor: JumpToLabelDescriptor,
    labels: Dict[BoolExprId, str],
) -> CodeBlock:
    cond_expr = ExprOperator(
        a=descriptor.bool_expr.a,
        b=descriptor.bool_expr.b,
        op="-",
        location=descriptor.bool_expr.location,
    )

    false_label = labels[descriptor.on_false]

    code_block += CodeBlock.singleton(
        CodeElementConditionalJump(
            label=ExprIdentifier(name=false_label, location=descriptor.bool_expr.location),
            condition=cond_expr,
            location=descriptor.bool_expr.location,
        )
    )

    if descriptor.on_true is not None:
        true_label = labels[descriptor.on_true]

        code_block += CodeBlock.singleton(
            CodeElementConditionalJump(
                label=ExprIdentifier(name=true_label, location=descriptor.bool_expr.location),
                condition=None,
                location=descriptor.bool_expr.location,
            )
        )

    return code_block


def _lower_terminal(
    code_block: CodeBlock,
    terminal: Terminal,
    elm: CodeElementIf,
    labels: Dict[BoolExprId, str],
) -> CodeBlock:
    case_code_block = elm.main_code_block if terminal.case else elm.else_code_block
    assert case_code_block is not None
    code_block += case_code_block

    if terminal.exit:
        exit_label = labels[terminal.exit]
        code_block += CodeBlock.singleton(
            CodeElementEraseIfUnreachable(
                CodeElementConditionalJump(
                    label=ExprIdentifier(name=exit_label, location=elm.location),
                    condition=None,
                    location=elm.location,
                )
            )
        )

    return code_block
