import dataclasses
from typing import Sequence, Optional

from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ArgList
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.ast.rvalue import RvalueFuncCall
from starkware.cairo.lang.compiler.error_handling import Location


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
class ForClauseIn(AstNode):
    identifier: ExprIdentifier
    generator: ForGeneratorRange

    @property
    def location(self) -> Optional[Location]:
        return self.identifier.location

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.identifier, self.generator]

    def get_particles(self):
        return [f"{self.identifier.format()} in ", *self.generator.get_particles()]
