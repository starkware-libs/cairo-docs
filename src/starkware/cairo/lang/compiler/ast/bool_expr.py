import dataclasses
from enum import Enum
from typing import Optional, Sequence, Union

from starkware.cairo.lang.compiler.ast.expr import Expression
from starkware.cairo.lang.compiler.ast.formatting_utils import LocationField, ParticleList
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location


@dataclasses.dataclass
class BoolEqExpr(AstNode):
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
class BoolAndExpr(AstNode):
    a: Union[BoolEqExpr, "BoolAndExpr"]
    b: BoolEqExpr
    location: Optional[Location] = LocationField

    def get_particles(self):
        return ParticleList([self.a.get_particles(), " and ", self.b.get_particles()])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]
