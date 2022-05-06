from typing import Tuple

from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr
from starkware.cairo.lang.compiler.ast.cairo_types import CairoType, TypeFelt
from starkware.cairo.lang.compiler.ast.code_elements import CodeBlock
from starkware.cairo.lang.compiler.ast.expr import (
    Expression,
    ExprConst,
    ExprAssignment,
    ExprIdentifier,
    ExprOperator,
)
from starkware.cairo.lang.compiler.ast.for_loop import ForGeneratorRange
from starkware.cairo.lang.compiler.error_handling import Location
from starkware.cairo.lang.compiler.preprocessor.for_loop.generators import GeneratorLowering
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError


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
