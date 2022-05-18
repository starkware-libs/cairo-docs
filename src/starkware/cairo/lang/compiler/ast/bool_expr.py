import dataclasses
from enum import Enum
from typing import Optional, Sequence, Union

from starkware.cairo.lang.compiler.ast.expr import Expression
from starkware.cairo.lang.compiler.ast.formatting_utils import LocationField, ParticleList
from starkware.cairo.lang.compiler.ast.node import AstNode
from starkware.cairo.lang.compiler.error_handling import Location


@dataclasses.dataclass
class BoolExpr(AstNode):
    a: Expression
    b: Expression
    eq: bool
    location: Optional[Location] = LocationField

    def get_particles(self):
        relation = "==" if self.eq else "!="
        return f"{self.a.format()} {relation} {self.b.format()}"

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]


class BoolProductOp(Enum):
    AND = "and"
    OR = "or"


@dataclasses.dataclass
class BoolProductExpr(AstNode):
    a: BoolExpr
    b: Union[BoolExpr, "BoolProductExpr"]
    op: BoolProductOp
    location: Optional[Location] = LocationField

    def get_particles(self):
        return ParticleList([self.a.get_particles(), f" {self.op.value} ", self.b.get_particles()])

    def get_children(self) -> Sequence[Optional[AstNode]]:
        return [self.a, self.b]
