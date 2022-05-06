import operator
from abc import ABC, abstractmethod
from functools import reduce
from typing import Tuple, Iterable, List, Optional

from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr
from starkware.cairo.lang.compiler.ast.cairo_types import CairoType, TypeFelt
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementFor,
    CodeElementFunction,
    CodeBlock,
    CodeElementReturn,
    CodeElementFuncCall,
    CodeElementIf,
    CodeElementTailCall,
    CodeElement,
    CodeElementReference,
)
from starkware.cairo.lang.compiler.ast.expr import (
    ExprIdentifier,
    Expression,
    ExprAssignment,
    ExprConst,
    ArgList,
    ExprOperator,
    ExprCast,
)
from starkware.cairo.lang.compiler.ast.for_loop import ForClauseIn, ForGeneratorRange
from starkware.cairo.lang.compiler.ast.notes import Notes
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.error_handling import LocationError, Location
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
    CodeElementsInjection,
)
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManagerContext, VisitorStage


class ForLoopLoweringError(LocationError):
    pass


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
        envelope, iterator_function = lower_for_loop(
            elm, implicit_arguments=self._borrow_current_implicit_args()
        )
        self.inject_function(iterator_function)
        return CodeElementsInjection.from_code_block(envelope)

    def _borrow_current_implicit_args(self) -> Optional[IdentifierList]:
        for parent in reversed(self.parents):
            if isinstance(parent, CodeElementFunction):
                return parent.implicit_arguments
            elif not isinstance(parent, CodeElement):
                # Try our best to avoid jumping to irrelevant function which somehow
                # was put in parents stack.
                break

        return None


def lower_for_loop(
    elm: CodeElementFor, implicit_arguments: Optional[IdentifierList] = None
) -> Tuple[CodeBlock, CodeElementFunction]:
    """
    Lowers for loops into calls to recursive functions.

    Lowering algorithm
    ==================

    The general rule, expressed in Cairo pseudocode would transform this::

        for $I : $T in {generator}:
            {instructions}
        END

    into following Cairo code::

        {initialize iterator if necessary}
        $F({starting iterator value}, {bound references...})

        # separate code section
        func $F($Iterator: {generator iterator type}, {bound references...}):
            {alloc_locals if necessary}

            {initialize condition if necessary}
            if {condition}:
                let $I = cast($Iterator, $T)  # or just $Iterator if $T was not specified

                {instructions}

                {initialize next($I) if necessary}
                return $F({next($I)}, {bound references...})
            else
                ret
            end
        end
    """

    in_clause = _fetch_in_clause(elm)
    bound_identifiers = _fetch_bound_identifiers(elm)

    low = InClauseLowering(in_clause)
    envelope = _build_envelope(elm, low, bound_identifiers=bound_identifiers)
    iterator_function = _build_iterator_function(
        elm, low, bound_identifiers=bound_identifiers, implicit_arguments=implicit_arguments
    )
    return envelope, iterator_function


class InClauseLowering:
    priv_iter_name: str
    iter_identifier: TypedIdentifier
    generator_location: Location
    generator: "GeneratorLowering"

    def __init__(self, clause: ForClauseIn):
        assert clause.label_iter is not None
        self.priv_iter_name = clause.label_iter
        self.iter_identifier = clause.identifier
        self.generator_location = clause.generator.location
        self.generator = GeneratorLowering.from_in_clause(clause)


class GeneratorLowering(ABC):
    @abstractmethod
    def iterator_type(self) -> CairoType:
        """
        Provide Cairo type of iterator values returned by this generator.
        """

    @abstractmethod
    def init_envelope_iterator(self) -> Tuple[CodeBlock, Expression]:
        """
        Provide Cairo code which initializes the iterator variable.
        """

    @abstractmethod
    def condition(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, BoolExpr]:
        """
        Provide Cairo code which checks if iteration reaches end.
        """

    @abstractmethod
    def increment_iterator(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, Expression]:
        """
        Provide Cairo code which increments iterator variable.
        """

    @staticmethod
    def from_in_clause(clause: ForClauseIn) -> "GeneratorLowering":
        generator = clause.generator
        if isinstance(generator, ForGeneratorRange):
            return RangeGeneratorLowering(generator)
        else:
            raise NotImplementedError(
                f"Lowering '{generator.func_ident.name}' generator is not implemented yet."
            )


class RangeGeneratorLowering(GeneratorLowering):
    generator_location: Location
    start: Expression
    stop: Expression
    step: Expression

    def __init__(self, generator: ForGeneratorRange):
        self.generator_location = generator.location

        args = generator.arguments.args

        # Validate arguments.
        if len(args) == 0:
            raise ForLoopLoweringError(
                "Range generator excepts at least the stop argument.",
                location=generator.location,
            )

        if len(args) > 3:
            assert args[3].location is not None and args[-1].location is not None
            excessive_args_location = args[3].location.span(args[-1].location)

            raise ForLoopLoweringError(
                "Too many arguments passed to range generator.", location=excessive_args_location
            )

        # TODO(mkaput, 21/04/2022): Support keyword arguments here.
        #   There is a refactoring opportunity here, as this functionality
        #   is implemented in process_expr_assignment_list in Preprocessor.
        #   As for now, we just error proactively.
        for arg in args:
            if arg.identifier is not None:
                raise ForLoopLoweringError(
                    "Keyword arguments are not supported here yet.", location=arg.location
                )

        # Pad arguments to 3 element list with None as filling. This will simplify further code.
        if len(args) < 2:
            args = [None, *args]
        if len(args) < 3:
            args = [*args, None]

        # Extract arguments and set defaults
        [start, stop, step] = args

        if start is None:
            self.start = ExprConst(val=0)
        else:
            assert isinstance(start, ExprAssignment)
            self.start = start.expr

        assert isinstance(stop, ExprAssignment)
        self.stop = stop.expr

        if step is None:
            self.step = ExprConst(val=1)
        else:
            assert isinstance(step, ExprAssignment)
            self.step = step.expr

    def iterator_type(self) -> CairoType:
        return TypeFelt(location=self.generator_location)

    def init_envelope_iterator(self) -> Tuple[CodeBlock, Expression]:
        return CodeBlock([]), self.start

    def condition(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, BoolExpr]:
        return CodeBlock([]), BoolExpr(
            eq=True, a=iter_expr, b=self.stop, location=self.generator_location
        )

    def increment_iterator(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, Expression]:
        return CodeBlock([]), ExprOperator(op="+", a=iter_expr, b=self.step)


# Common codegen utilities.


def _priv_iter_name_body(low: InClauseLowering) -> ExprIdentifier:
    return ExprIdentifier(name=low.priv_iter_name, location=low.iter_identifier.location)


def _iterator_function_identifier(elm: CodeElementFor) -> ExprIdentifier:
    return ExprIdentifier(name=elm.label_func, location=elm.location)


def _expr_assignments_from_typed_identifiers(
    identifiers: Iterable[TypedIdentifier],
) -> List[ExprAssignment]:
    return [
        ExprAssignment(identifier=ident.identifier, expr=ident.identifier, location=ident.location)
        for ident in identifiers
    ]


# Clauses processing.


def _fetch_in_clause(elm: CodeElementFor) -> ForClauseIn:
    in_clauses = elm.clauses.in_clauses()

    if not in_clauses:
        raise ForLoopLoweringError("For loop requires one 'in' clause.", location=elm.location)

    if len(in_clauses) > 1:
        extra_clauses_location = in_clauses[1].location.span(in_clauses[-1].location)
        raise ForLoopLoweringError(
            "Multiple 'in' clauses in for loops are not supported.", location=extra_clauses_location
        )

    return in_clauses[0]


def _fetch_bound_identifiers(elm: CodeElementFor) -> List[TypedIdentifier]:
    identifier_groups = (clause.identifiers.identifiers for clause in elm.clauses.bind_clauses())
    return reduce(operator.add, identifier_groups, [])


# Envelope generation.


def _build_envelope(
    elm: CodeElementFor, low: InClauseLowering, bound_identifiers: List[TypedIdentifier]
) -> CodeBlock:
    iterator_init, iterator_expr = low.generator.init_envelope_iterator()
    return iterator_init + CodeBlock.singleton(
        CodeElementFuncCall(
            func_call=RvalueFuncCall(
                func_ident=_iterator_function_identifier(elm),
                arguments=ArgList.from_args(
                    args=[
                        ExprAssignment(
                            identifier=_priv_iter_name_body(low),
                            expr=iterator_expr,
                            location=low.iter_identifier.location,
                        ),
                        *_expr_assignments_from_typed_identifiers(bound_identifiers),
                    ],
                    location=elm.location,
                ),
                implicit_arguments=None,
                location=elm.location,
            )
        )
    )


# Iterator function generation.


def _build_iterator_function(
    elm: CodeElementFor,
    low: InClauseLowering,
    bound_identifiers: List[TypedIdentifier],
    implicit_arguments: Optional[IdentifierList] = None,
) -> CodeElementFunction:
    assert elm.label_func is not None
    assert elm.label_if_neq is not None
    assert elm.label_if_end is not None

    arguments = IdentifierList(
        identifiers=[
            TypedIdentifier(
                identifier=_priv_iter_name_body(low),
                expr_type=low.generator.iterator_type(),
                location=low.iter_identifier.location,
            ),
            *bound_identifiers,
        ],
        location=elm.location,
    )

    condition_init, condition_expr = low.generator.condition(iter_expr=_priv_iter_name_body(low))
    next_init, next_expr = low.generator.increment_iterator(iter_expr=_priv_iter_name_body(low))
    bind_iter_block = _bind_iter(low)
    body_block_init, body_block = _prepare_body(elm.code_block)

    code_block = (
        body_block_init
        + condition_init
        + CodeBlock.singleton(
            CodeElementIf(
                condition=condition_expr,
                main_code_block=(
                    bind_iter_block
                    + body_block
                    + next_init
                    + CodeBlock.singleton(
                        _tail_call_iterator_function(elm, low, next_expr, bound_identifiers),
                    )
                ),
                else_code_block=(
                    CodeBlock.singleton(
                        CodeElementReturn(exprs=[], location=elm.location),
                    )
                ),
                label_neq=elm.label_if_neq,
                label_end=elm.label_if_end,
                location=elm.location,
            ),
        )
    )

    return CodeElementFunction(
        element_type="func",
        identifier=_iterator_function_identifier(elm),
        arguments=arguments,
        implicit_arguments=implicit_arguments,
        returns=None,
        code_block=code_block,
        decorators=[],
    )


def _bind_iter(low: InClauseLowering) -> CodeBlock:
    priv_iter_expr = _priv_iter_name_body(low)

    # We only have to cast if user explicitly provided iterator type
    if low.iter_identifier.expr_type is not None:
        cast_expr = ExprCast(
            expr=priv_iter_expr,
            dest_type=low.iter_identifier.expr_type,
            notes=Notes(),
            location=low.iter_identifier.location,
        )
    else:
        cast_expr = priv_iter_expr

    return CodeBlock.from_code_elements(
        [
            CodeElementReference(
                typed_identifier=low.iter_identifier,
                expr=cast_expr,
            )
        ]
    )


def _prepare_body(code_block: CodeBlock) -> Tuple[CodeBlock, CodeBlock]:
    return CodeBlock.from_code_elements([]), code_block


def _tail_call_iterator_function(
    elm: CodeElementFor,
    low: InClauseLowering,
    next_expr: Expression,
    bound_identifiers: List[TypedIdentifier],
) -> CodeElementTailCall:
    return CodeElementTailCall(
        func_call=RvalueFuncCall(
            func_ident=_iterator_function_identifier(elm),
            arguments=ArgList.from_args(
                args=[
                    ExprAssignment(
                        identifier=_priv_iter_name_body(low),
                        expr=next_expr,
                        location=low.iter_identifier.location,
                    ),
                    *_expr_assignments_from_typed_identifiers(bound_identifiers),
                ],
                location=elm.location,
            ),
            implicit_arguments=None,
            location=elm.location,
        ),
        location=elm.location,
    )
