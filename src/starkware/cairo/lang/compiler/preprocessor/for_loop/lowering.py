from typing import Iterable, List, Optional

from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.cairo_types import CairoType
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementFor,
    CodeElementFunction,
    CodeBlock,
    CodeElementReturn,
    CodeElementFuncCall,
    CodeElementIf,
    CodeElementTailCall,
    CodeElementReference,
    CodeElementAllocLocals,
)
from starkware.cairo.lang.compiler.ast.expr import (
    ExprIdentifier,
    ExprAssignment,
    ArgList,
    ExprCast,
)
from starkware.cairo.lang.compiler.ast.module import CairoModule
from starkware.cairo.lang.compiler.ast.notes import Notes
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
    CodeElementInjection,
)
from starkware.cairo.lang.compiler.preprocessor.for_loop.clauses import (
    InClauseLowering,
    fetch_in_clause,
    fetch_bound_identifiers,
)
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManagerContext, VisitorStage
from starkware.cairo.lang.compiler.unique_name_provider import UniqueNameKind


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
        current_function = self._get_current_function(elm)

        # Borrow implicit arguments of for loop body from current function.
        implicit_arguments = current_function.implicit_arguments

        in_clause = fetch_in_clause(elm=elm)
        bound_identifiers = fetch_bound_identifiers(elm=elm)

        lowering = InClauseLowering.from_clause(clause=in_clause)

        _check_body_has_no_alloc_locals(code_block=elm.code_block)

        iterator_function_identifier = ExprIdentifier(
            name=self.context.unique_names.next(UniqueNameKind.Func), location=elm.location
        )

        iterator_types = lowering.generator.declare_iterator()
        iterator_variables = [
            ExprIdentifier(
                name=self.context.unique_names.next(UniqueNameKind.Var),
                location=lowering.generator_location,
            )
            for _ in iterator_types
        ]

        envelope = _build_envelope(
            elm=elm,
            lowering=lowering,
            iterator_function_identifier=iterator_function_identifier,
            iterator_variables=iterator_variables,
            bound_identifiers=bound_identifiers,
        )

        iterator_function = _build_iterator_function(
            elm=elm,
            lowering=lowering,
            iterator_function_identifier=iterator_function_identifier,
            iterator_variables=iterator_variables,
            iterator_types=iterator_types,
            bound_identifiers=bound_identifiers,
            implicit_arguments=implicit_arguments,
        )

        self.inject_function(iterator_function)
        return CodeElementInjection.from_code_block(envelope)

    def _get_current_function(self, elm: CodeElementFor) -> CodeElementFunction:
        for parent in reversed(self.parents):
            if isinstance(parent, CodeElementFunction):
                return parent
            if isinstance(parent, CairoModule):
                break

        raise ForLoopLoweringError(
            "For loops are unsupported outside functions.", location=elm.location
        )


def _expr_assignments_from_typed_identifiers(
    identifiers: Iterable[TypedIdentifier],
) -> List[ExprAssignment]:
    return [
        ExprAssignment(identifier=ident.identifier, expr=ident.identifier, location=ident.location)
        for ident in identifiers
    ]


def _build_envelope(
    elm: CodeElementFor,
    lowering: InClauseLowering,
    iterator_function_identifier: ExprIdentifier,
    iterator_variables: List[ExprIdentifier],
    bound_identifiers: List[TypedIdentifier],
) -> CodeBlock:
    iterator_init, iterator_exprs = lowering.generator.init_envelope_iterator()
    iterator_args = [
        ExprAssignment(
            identifier=identifier,
            expr=expr,
            location=lowering.iter_identifier.location,
        )
        for identifier, expr in zip(iterator_variables, iterator_exprs)
    ]
    bound_args = _expr_assignments_from_typed_identifiers(bound_identifiers)
    return iterator_init + CodeBlock.singleton(
        CodeElementFuncCall(
            func_call=RvalueFuncCall(
                func_ident=iterator_function_identifier,
                arguments=ArgList.from_args(
                    args=iterator_args + bound_args,
                    location=elm.location,
                ),
                implicit_arguments=None,
                location=elm.location,
            )
        )
    )


def _build_iterator_function(
    elm: CodeElementFor,
    lowering: InClauseLowering,
    iterator_function_identifier: ExprIdentifier,
    iterator_variables: List[ExprIdentifier],
    iterator_types: List[CairoType],
    bound_identifiers: List[TypedIdentifier],
    implicit_arguments: Optional[IdentifierList] = None,
) -> CodeElementFunction:
    iterator_args = [
        TypedIdentifier(
            identifier=identifier,
            expr_type=expr_type,
            location=lowering.iter_identifier.location,
        )
        for identifier, expr_type in zip(iterator_variables, iterator_types)
    ]
    arguments = IdentifierList(
        identifiers=iterator_args + bound_identifiers,
        location=elm.location,
    )

    condition_init, condition_expr = lowering.generator.condition(*iterator_variables)
    next_init, next_exprs = lowering.generator.increment_iterator(*iterator_variables)
    bind_iter_block = _bind_iter(lowering, iterator_variables)

    iterator_call_args = [
        ExprAssignment(
            identifier=identifier,
            expr=expr,
            location=lowering.iter_identifier.location,
        )
        for identifier, expr in zip(iterator_variables, next_exprs)
    ]
    tail_call_block = CodeBlock.singleton(
        CodeElementTailCall(
            func_call=RvalueFuncCall(
                func_ident=iterator_function_identifier,
                arguments=ArgList.from_args(
                    args=iterator_call_args
                    + _expr_assignments_from_typed_identifiers(bound_identifiers),
                    location=elm.location,
                ),
                implicit_arguments=None,
                location=elm.location,
            ),
            location=elm.location,
        ),
    )

    code_block = (
        CodeBlock.singleton(CodeElementAllocLocals(location=elm.location))
        + condition_init
        + CodeBlock.singleton(
            CodeElementIf(
                condition=condition_expr,
                main_code_block=(
                    CodeBlock.singleton(
                        CodeElementReturn(exprs=[], location=elm.location),
                    )
                ),
                else_code_block=(bind_iter_block + elm.code_block + next_init + tail_call_block),
                location=elm.location,
            ),
        )
    )

    return CodeElementFunction(
        element_type="func",
        identifier=iterator_function_identifier,
        arguments=arguments,
        implicit_arguments=implicit_arguments,
        returns=None,
        code_block=code_block,
        decorators=[],
    )


def _bind_iter(lowering: InClauseLowering, iterator_variables: List[ExprIdentifier]) -> CodeBlock:
    bound_expr = lowering.generator.bind_iterator(*iterator_variables)

    # We only have to cast if user explicitly provided iterator type
    if lowering.iter_identifier.expr_type is not None:
        cast_expr = ExprCast(
            expr=bound_expr,
            dest_type=lowering.iter_identifier.expr_type,
            notes=Notes(),
            location=lowering.iter_identifier.location,
        )
    else:
        cast_expr = bound_expr

    return CodeBlock.from_code_elements(
        [
            CodeElementReference(
                typed_identifier=lowering.iter_identifier,
                expr=cast_expr,
            )
        ]
    )


def _check_body_has_no_alloc_locals(code_block: CodeBlock):
    elms = code_block.code_elements
    if len(elms) > 0 and isinstance(elms[0].code_elm, CodeElementAllocLocals):
        raise ForLoopLoweringError(
            "alloc_locals is not allowed in the body of a for loop.",
            location=elms[0].location,
        )
