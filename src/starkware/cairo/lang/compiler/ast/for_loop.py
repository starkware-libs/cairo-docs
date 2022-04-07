import dataclasses
from typing import Sequence, Optional

from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, Expression
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location
from starkware.python.expression_string import ExpressionString


@dataclasses.dataclass
class ForGeneratorRange(Expression):
    start: Optional[Expression]
    stop: Expression
    step: Optional[Expression]
    location: Optional[Location]

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return self.get_arguments()

    def get_arguments(self) -> Sequence[Expression]:
        args = []

        if self.start is not None:
            args.append(self.start)

        args.append(self.stop)

        if self.step is not None:
            args.append(self.step)

        return args

    def to_expr_str(self) -> ExpressionString:
        # TODO: Better line breaking for arguments
        args = ", ".join([child.format() for child in self.get_arguments()])
        return ExpressionString.highest(f"range({args})")


@dataclasses.dataclass
class ForClauseIn(AstNode):
    identifier: ExprIdentifier
    generator: ForGeneratorRange

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return [f"{self.identifier.format()} in ", self.generator.format()]
