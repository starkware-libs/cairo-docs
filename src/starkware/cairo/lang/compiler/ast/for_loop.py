import dataclasses
from typing import Sequence, Optional, Tuple

from starkware.cairo.lang.compiler.ast.arguments import CommaSeparatedWithNotes
from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, Expression
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location


@dataclasses.dataclass
class ForGeneratorRange(AstNode):
    args: CommaSeparatedWithNotes
    location: Optional[Location]

    @property
    def start(self) -> Optional[Expression]:
        return self.args_or_nones[0]

    @property
    def stop(self) -> Expression:
        return self.args_or_nones[1]

    @property
    def step(self) -> Optional[Expression]:
        return self.args_or_nones[2]

    @property
    def args_or_nones(self) -> Tuple[Optional[Expression], Expression, Optional[Expression]]:
        """
        Returns (start, stop, step) arguments tuple, with `None` if argument was not provided.
        """
        args = self.args.args
        if len(args) < 2:
            args = [None, *args]
        if len(args) < 3:
            args = [*args, None]
        return tuple(args)

    def get_children(self) -> Sequence[Expression]:
        return self.args.args

    def format(self):
        # TODO(mkaput, 08/04/2022): Better line breaking for arguments
        args = ", ".join([child.format() for child in self.get_children()])
        return f"range({args})"


@dataclasses.dataclass
class ForClauseIn(AstNode):
    identifier: ExprIdentifier
    generator: ForGeneratorRange
    location: Optional[Location]

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return [f"{self.identifier.format()} in ", self.generator.format()]
