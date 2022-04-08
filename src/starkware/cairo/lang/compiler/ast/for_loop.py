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
