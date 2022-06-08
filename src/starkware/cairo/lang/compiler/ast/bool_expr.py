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
    """
    Base class for all boolean expressions.
    """

    location: Optional[Location] = LocationField

    @abstractmethod
    def to_particle(self) -> Particle:
        """
        Get formatting particle for this expression.
        """

    @abstractmethod
    def first_bool_leaf(self) -> "BoolEqExpr":
        """
        Get the first leaf ``BoolEqExpr`` in this boolean expression which will be evaluated.
        """


@dataclasses.dataclass
class BoolEqExpr(BoolExpr):
    """
    Represents a trivial (in)equality comparison between two expressions.

    This is the most primitive building block of conditions in ``if`` code element.
    """

    a: Expression
    b: Expression
    eq: bool
    notes: Notes = NotesField
    location: Optional[Location] = LocationField

    def to_particle(self) -> Particle:
        self.notes.assert_no_comments()
        relation = "==" if self.eq else "!="
        return SingleParticle(f"{self.a.format()} {relation} {self.b.format()}")

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]

    def first_bool_leaf(self) -> "BoolEqExpr":
        return self


@dataclasses.dataclass
class BoolAndExpr(BoolExpr):
    """
    Represents logical *and* of two ``BoolExpr``s (``and`` operator).
    """

    a: BoolExpr
    b: BoolExpr
    notes: Notes = NotesField
    location: Optional[Location] = LocationField

    def to_particle(self) -> Particle:
        self.notes.assert_no_comments()
        a = self.a.to_particle()
        a.add_suffix(" and ")
        b = self.b.to_particle()
        return ParticleList([a, b])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]

    def first_bool_leaf(self) -> "BoolEqExpr":
        return self.a.first_bool_leaf()


# TODO(mkaput, 03/06/2022): Add grammar support for or expressions.
@dataclasses.dataclass
class BoolOrExpr(BoolExpr):
    """
    Represents logical *or* of two ``BoolExpr``s (``or`` operator).
    """

    a: BoolExpr
    b: BoolExpr
    notes: Notes = NotesField
    location: Optional[Location] = LocationField

    def to_particle(self) -> Particle:
        self.notes.assert_no_comments()
        a = self.a.to_particle()
        a.add_suffix(" or ")
        b = self.b.to_particle()
        return ParticleList([a, b])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]

    def first_bool_leaf(self) -> "BoolEqExpr":
        return self.a.first_bool_leaf()
