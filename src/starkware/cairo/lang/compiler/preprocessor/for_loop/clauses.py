import dataclasses
import itertools
from typing import List

from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFor
from starkware.cairo.lang.compiler.ast.for_loop import ForClauseIn
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.error_handling import Location
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.for_loop.generators import GeneratorLowering


@dataclasses.dataclass
class InClauseLowering:
    iter_identifier: TypedIdentifier
    generator_location: Location
    generator: GeneratorLowering

    @classmethod
    def from_clause(cls, clause: ForClauseIn) -> "InClauseLowering":
        return cls(
            iter_identifier=clause.identifier,
            generator_location=clause.generator.location,
            generator=GeneratorLowering.from_in_clause(clause),
        )


def fetch_in_clause(elm: CodeElementFor) -> ForClauseIn:
    in_clauses = elm.clauses.in_clauses()

    if len(in_clauses) == 0:
        raise ForLoopLoweringError("For loop requires one 'in' clause.", location=elm.location)

    if len(in_clauses) > 1:
        extra_clauses_location = in_clauses[1].location.span(in_clauses[-1].location)
        raise ForLoopLoweringError(
            "Multiple 'in' clauses in for loops are not supported.", location=extra_clauses_location
        )

    return in_clauses[0]


def fetch_bound_identifiers(elm: CodeElementFor) -> List[TypedIdentifier]:
    identifier_groups = (clause.identifiers.identifiers for clause in elm.clauses.with_clauses())
    return list(itertools.chain.from_iterable(identifier_groups))
