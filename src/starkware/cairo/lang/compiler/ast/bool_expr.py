import dataclasses
from abc import ABC, abstractmethod
from typing import Optional, Sequence

from starkware.cairo.lang.compiler.ast.expr import Expression
from starkware.cairo.lang.compiler.ast.formatting_utils import (
    LocationField,
    ParticleList,
    Particle,
    SingleParticle,
)
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.ast.notes import NotesField, Notes
from starkware.cairo.lang.compiler.error_handling import Location


class BoolExpr(AstNode, ABC):
    location: Optional[Location] = LocationField

    @abstractmethod
    def to_particle(self) -> Particle:
        """
        Get formatting particle for this expression.
        """


@dataclasses.dataclass
class BoolEqExpr(BoolExpr):
    a: Expression
    b: Expression
    eq: bool
    notes: Notes = NotesField
    location: Optional[Location] = LocationField

    def to_particle(self):
        self.notes.assert_no_comments()
        relation = "==" if self.eq else "!="
        return SingleParticle(f"{self.a.format()} {relation} {self.b.format()}")

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]


@dataclasses.dataclass
class BoolAndExpr(BoolExpr):
    a: BoolExpr
    b: BoolEqExpr
    notes: Notes = NotesField
    location: Optional[Location] = LocationField

    def to_particle(self):
        self.notes.assert_no_comments()
        return ParticleList([self.a.to_particle(), " and ", self.b.to_particle()])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]
