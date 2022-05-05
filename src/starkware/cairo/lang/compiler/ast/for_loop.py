import dataclasses
from abc import ABC, abstractmethod
from typing import Sequence, Optional, List

from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ArgList
from starkware.cairo.lang.compiler.ast.formatting_utils import (
    LocationField,
    SeparatedParticleList,
    ParticleList,
    Particles,
)
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.ast.notes import Notes, NoteListField
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.error_handling import Location


class ForClause(AstNode, ABC):
    location: Optional[Location]

    @abstractmethod
    def get_particles(self) -> Particles:
        """
        Returns formatting particles for this clause.
        """


@dataclasses.dataclass
class ForClausesList(AstNode):
    clauses: List[ForClause]
    notes: List[Notes] = NoteListField
    location: Optional[Location] = LocationField

    def assert_no_comments(self):
        for note in self.notes:
            note.assert_no_comments()

    def get_particles(self) -> SeparatedParticleList:
        self.assert_no_comments()

        def clause_order(clause: ForClause):
            order = [ForClauseIn, ForClauseBind]
            return order.index(type(clause))

        return SeparatedParticleList(
            elements=[clause.get_particles() for clause in (sorted(self.clauses, key=clause_order))]
        )

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return self.clauses

    def in_clauses(self) -> List["ForClauseIn"]:
        return [clause for clause in self.clauses if isinstance(clause, ForClauseIn)]

    def bind_clauses(self) -> List["ForClauseBind"]:
        return [clause for clause in self.clauses if isinstance(clause, ForClauseBind)]

    @classmethod
    def from_clauses(cls, clauses: List[ForClause], **kwargs) -> "ForClausesList":
        notes = [Notes() for _ in range(len(clauses) + 1)]
        return cls(clauses=clauses, notes=notes, **kwargs)


@dataclasses.dataclass
class ForGenerator(RvalueFuncCall, ABC):
    pass


@dataclasses.dataclass
class ForGeneratorRange(ForGenerator):
    def __post_init__(self):
        assert self.func_ident.name == "range"
        assert self.implicit_arguments is None

    @classmethod
    def from_arguments(cls, arguments: ArgList, **kwargs) -> "ForGeneratorRange":
        return cls(
            func_ident=ExprIdentifier(name="range"),
            arguments=arguments,
            implicit_arguments=None,
            **kwargs,
        )


@dataclasses.dataclass
class ForGeneratorSlice(ForGenerator):
    def __post_init__(self):
        assert self.func_ident.name == "slice"
        assert self.implicit_arguments is None

    @classmethod
    def from_arguments(cls, arguments: ArgList, **kwargs) -> "ForGeneratorSlice":
        return cls(
            func_ident=ExprIdentifier(name="slice"),
            arguments=arguments,
            implicit_arguments=None,
            **kwargs,
        )


@dataclasses.dataclass
class ForClauseIn(ForClause):
    identifier: TypedIdentifier
    generator: ForGenerator
    location: Optional[Location] = LocationField
    label_iter: Optional[str] = None

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return ParticleList([f"{self.identifier.format()} in ", *self.generator.get_particles()])


@dataclasses.dataclass
class ForClauseBind(ForClause):
    identifiers: IdentifierList
    location: Optional[Location] = LocationField

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifiers]

    def get_particles(self):
        return SeparatedParticleList(
            start="local(", elements=self.identifiers.get_particles(), end=")"
        )
