from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr
from starkware.cairo.lang.compiler.ast.cairo_types import TypeFelt, TypePointer
from starkware.cairo.lang.compiler.ast.code_elements import CodeBlock
from starkware.cairo.lang.compiler.ast.expr import (
    Expression,
    ExprConst,
    ExprAssignment,
    ExprIdentifier,
    ExprOperator,
)
from starkware.cairo.lang.compiler.ast.for_loop import ForGeneratorSlice
from starkware.cairo.lang.compiler.error_handling import Location
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.for_loop.generators import GeneratorLowering


class SliceGeneratorLowering(GeneratorLowering):
    location: Location
    array: Expression
    number: Expression
    size: Expression

    def __init__(self, generator: ForGeneratorSlice):
        self.location = generator.location

        args = generator.arguments.args

        # Validate arguments.
        if len(args) < 2:
            raise ForLoopLoweringError(
                "Slice generator expects at least 'array' and 'number' arguments.",
                location=generator.location,
            )

        if len(args) > 3:
            assert args[3].location is not None and args[-1].location is not None
            excessive_args_location = args[3].location.span(args[-1].location)

            raise ForLoopLoweringError(
                "Too many arguments passed to slice generator.", location=excessive_args_location
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
        if len(args) < 3:
            args = [*args, None]

        # Extract arguments and set defaults
        [array, number, size] = args

        assert isinstance(array, ExprAssignment)
        self.array = array.expr

        assert isinstance(number, ExprAssignment)
        self.number = number.expr

        if size is None:
            self.size = ExprConst(val=1)
        else:
            assert isinstance(size, ExprAssignment)
            self.size = size.expr

    def declare_iterator(self):
        return [
            # current
            TypePointer(TypeFelt(location=self.location), location=self.location),
            # end
            TypePointer(TypeFelt(location=self.location), location=self.location),
        ]

    def init_envelope_iterator(self):
        return CodeBlock(), [
            # current
            self.array,
            # end
            ExprOperator(
                op="+",
                a=self.array,
                b=ExprOperator(op="*", a=self.number, b=self.size, location=self.location),
                location=self.location,
            ),
        ]

    def condition(self, current: ExprIdentifier, end: ExprIdentifier):
        return CodeBlock([]), BoolExpr(eq=True, a=current, b=end, location=self.location)

    def bind_iterator(self, current: ExprIdentifier, _end: ExprIdentifier):
        return current

    def increment_iterator(self, current: ExprIdentifier, end: ExprIdentifier):
        return CodeBlock(), [ExprOperator(op="+", a=current, b=self.size), end]
