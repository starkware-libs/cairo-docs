from typing import List, Tuple

from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr
from starkware.cairo.lang.compiler.ast.cairo_types import CairoType, TypeFelt
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElement,
    CodeElementFor,
    CodeElementFunction,
    CodeBlock,
    CodeElementReturn,
    CodeElementFuncCall,
    CodeElementIf,
    CodeElementTailCall,
)
from starkware.cairo.lang.compiler.ast.expr import (
    ExprIdentifier,
    Expression,
    ExprAssignment,
    ExprConst,
    ArgList,
    ExprOperator,
)
from starkware.cairo.lang.compiler.ast.for_loop import ForClauseIn, ForGeneratorRange
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.error_handling import LocationError, Location
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
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
        envelope, iterator_function = lower_for_loop(elm)
        self.inject_function(iterator_function)
        return envelope


def lower_for_loop(elm: CodeElementFor) -> Tuple[List[CodeElement], CodeElementFunction]:
    """
    Lowers for loops into calls to recursive functions.

    Lowering algorithm
    ==================

    The general rule, expressed in Cairo pseudocode would transform this::

        for $I in {generator}:
            {instructions}
        END

    into following Cairo code::

        {initialize iterator if necessary}
        $F({starting iterator value})

        # separate code section
        func $F($I: $Iterator):
            {alloc_locals if necessary}

            {initialize condition if necessary}
            if {condition}:
                {instructions}

                {initialize next($I) if necessary}
                return $F({next($I)})
            else
                ret
            end
        end
    """

    in_clause = _fetch_in_clause(elm)

    gl = InRangeLowering(clause=in_clause)
    envelope = _build_envelope(elm, gl)
    envelope = [c.code_elm for c in envelope.code_elements]
    iterator_function = _build_iterator_function(elm, gl)
    return envelope, iterator_function


class InRangeLowering:
    iter_name_body: str
    iterator_location: Location
    generator_location: Location
    start: Expression
    stop: Expression
    step: Expression

    def __init__(self, clause: ForClauseIn):
        self.iter_name_body = clause.identifier.name

        self.iterator_location = clause.identifier.location
        self.generator_location = clause.generator.location

        generator = clause.generator
        assert isinstance(generator, ForGeneratorRange)

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


def _iter_name_body(gl: InRangeLowering) -> ExprIdentifier:
    return ExprIdentifier(name=gl.iter_name_body, location=gl.iterator_location)


def _iterator_function_identifier(elm: CodeElementFor) -> ExprIdentifier:
    return ExprIdentifier(name=elm.label_func, location=elm.location)


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


# Envelope generation.


def _build_envelope(elm: CodeElementFor, gl: InRangeLowering) -> CodeBlock:
    iterator_init, iterator_expr = gl.init_envelope_iterator()
    return iterator_init + CodeBlock.singleton(
        CodeElementFuncCall(
            func_call=RvalueFuncCall(
                func_ident=_iterator_function_identifier(elm),
                arguments=ArgList.from_args(
                    args=[
                        ExprAssignment(
                            identifier=_iter_name_body(gl),
                            expr=iterator_expr,
                            location=gl.iterator_location,
                        )
                    ],
                    location=elm.location,
                ),
                implicit_arguments=None,
                location=elm.location,
            )
        )
    )


# Iterator function generation.


def _build_iterator_function(elm: CodeElementFor, gl: InRangeLowering) -> CodeElementFunction:
    assert elm.label_func is not None
    assert elm.label_if_neq is not None
    assert elm.label_if_end is not None

    arguments = IdentifierList(
        identifiers=[
            TypedIdentifier(
                identifier=_iter_name_body(gl),
                expr_type=gl.iterator_type(),
                location=gl.iterator_location,
            )
        ],
        location=elm.location,
    )

    condition_init, condition_expr = gl.condition(iter_expr=_iter_name_body(gl))
    next_init, next_expr = gl.increment_iterator(iter_expr=_iter_name_body(gl))
    body_block_init, body_block = _prepare_body(elm.code_block)

    code_block = (
        body_block_init
        + condition_init
        + CodeBlock.singleton(
            CodeElementIf(
                condition=condition_expr,
                main_code_block=(
                    body_block
                    + next_init
                    + CodeBlock.singleton(
                        _tail_call_iterator_function(elm, gl, next_expr),
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
        # TODO(mkaput, 22/04/2022): Implement implicit arguments in for loops.
        implicit_arguments=None,
        returns=None,
        code_block=code_block,
        decorators=[],
    )


def _prepare_body(code_block: CodeBlock) -> Tuple[CodeBlock, CodeBlock]:
    return CodeBlock.from_code_elements([]), code_block


def _tail_call_iterator_function(
    elm: CodeElementFor, gl: InRangeLowering, next_expr: Expression
) -> CodeElementTailCall:
    return CodeElementTailCall(
        func_call=RvalueFuncCall(
            func_ident=_iterator_function_identifier(elm),
            arguments=ArgList.from_args(
                args=[
                    ExprAssignment(
                        identifier=_iter_name_body(gl),
                        expr=next_expr,
                        location=gl.iterator_location,
                    )
                ],
                location=elm.location,
            ),
            implicit_arguments=None,
            location=elm.location,
        ),
        location=elm.location,
    )
