import dataclasses
from abc import ABC, abstractmethod
from typing import Sequence, Optional, List

from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ArgList
from starkware.cairo.lang.compiler.ast.formatting_utils import (
    LocationField,
    SeparatedParticleList,
    ParticleList,
)
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.ast.notes import Notes, NoteListField
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.error_handling import Location


class ForClause(AstNode, ABC):
    location: Optional[Location]

    @abstractmethod
    def get_particles(self):
        ...


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
        return SeparatedParticleList(
            elements=[ParticleList(clause.get_particles()) for clause in self.clauses]
        )

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return self.clauses

    @classmethod
    def from_clauses(cls, clauses: List[ForClause], **kwargs) -> "ForClausesList":
        notes = [Notes() for _ in range(len(clauses) + 1)]
        return cls(clauses=clauses, notes=notes, **kwargs)


@dataclasses.dataclass
class ForGeneratorRange(RvalueFuncCall):
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
class ForClauseIn(ForClause):
    identifier: ExprIdentifier
    generator: ForGeneratorRange
    location: Optional[Location] = LocationField

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return [f"{self.identifier.format()} in ", *self.generator.get_particles()]
