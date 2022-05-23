import dataclasses
from abc import ABC, abstractmethod
from typing import Optional, Sequence

from starkware.cairo.lang.compiler.ast.expr import Expression
from starkware.cairo.lang.compiler.ast.formatting_utils import (
    LocationField,
    ParticleList,
    Particles,
)
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location


class BoolExpr(AstNode, ABC):
    location: Optional[Location] = LocationField

    @abstractmethod
    def get_particles(self) -> Particles:
        """
        Get formatting particles for this expression.
        """


@dataclasses.dataclass
class BoolEqExpr(BoolExpr):
    a: Expression
    b: Expression
    eq: bool
    location: Optional[Location] = LocationField

    def get_particles(self):
        relation = "==" if self.eq else "!="
        return f"{self.a.format()} {relation} {self.b.format()}"

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]


@dataclasses.dataclass
class BoolAndExpr(BoolExpr):
    a: BoolExpr
    b: BoolEqExpr
    location: Optional[Location] = LocationField

    def get_particles(self):
        return ParticleList([self.a.get_particles(), " and ", self.b.get_particles()])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]
