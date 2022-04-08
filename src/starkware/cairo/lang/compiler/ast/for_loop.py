import dataclasses
from typing import Sequence, Optional

from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ArgList
from starkware.cairo.lang.compiler.ast.formatting_utils import (
    ParticleList,
    SeparatedParticleList,
    LocationField,
)
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location


@dataclasses.dataclass
class ForGeneratorRange(AstNode):
    args: ArgList
    location: Optional[Location] = LocationField

    # def __post_init__(self):
    #     # Validate arguments.
    #     args = self.args.args
    #
    #     if len(args) == 0:
    #         raise LocationError(
    #             "Range generator excepts at least the stop argument.", location=self.location
    #         )
    #
    #     if len(args) > 3:
    #         assert args[3].location is not None and args[-1].location is not None
    #         excessive_args_location = args[3].location.span(args[-1].location)
    #
    #         raise LocationError(
    #             "Too many arguments passed to range generator.", location=excessive_args_location
    #         )
    #
    # @property
    # def start(self) -> Optional[Expression]:
    #     return self.args_or_nones[0]
    #
    # @property
    # def stop(self) -> Expression:
    #     return self.args_or_nones[1]
    #
    # @property
    # def step(self) -> Optional[Expression]:
    #     return self.args_or_nones[2]
    #
    # @property
    # def args_or_nones(self) -> Tuple[Optional[Expression], Expression, Optional[Expression]]:
    #     """
    #     Returns (start, stop, step) arguments tuple, with `None` if argument was not provided.
    #     """
    #     args = self.args.args
    #     if len(args) < 2:
    #         args = [None, *args]
    #     if len(args) < 3:
    #         args = [*args, None]
    #     return tuple(args)

    def get_children(self):
        return self.args

    def get_particles(self):
        self.args.assert_no_comments()
        return ParticleList(
            elements=[
                "range(",
                SeparatedParticleList(elements=[x.format() for x in self.args.args], end=")"),
            ]
        )


@dataclasses.dataclass
class ForClauseIn(AstNode):
    identifier: ExprIdentifier
    generator: ForGeneratorRange
    location: Optional[Location] = LocationField

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return [f"{self.identifier.format()} in ", self.generator.get_particles()]
