from abc import ABC, abstractmethod
from typing import Tuple, List

from starkware.cairo.lang.compiler.ast.bool_expr import BoolExpr
from starkware.cairo.lang.compiler.ast.cairo_types import CairoType
from starkware.cairo.lang.compiler.ast.code_elements import CodeBlock
from starkware.cairo.lang.compiler.ast.expr import Expression, ExprIdentifier
from starkware.cairo.lang.compiler.ast.for_loop import (
    ForClauseIn,
    ForGeneratorRange,
    ForGeneratorSlice,
)


class GeneratorLowering(ABC):
    @abstractmethod
    def declare_iterator(self) -> List[CairoType]:
        """
        Provide Cairo types of all iterator variables.
        """

    @abstractmethod
    def init_envelope_iterator(self) -> Tuple[CodeBlock, List[Expression]]:
        """
        Provide Cairo code which initializes iterator variables.
        """

    @abstractmethod
    def condition(self, *iters: ExprIdentifier) -> Tuple[CodeBlock, BoolExpr]:
        """
        Provide Cairo code which checks if iteration reaches end.
        """

    @abstractmethod
    def bind_iterator(self, *iters: ExprIdentifier) -> Expression:
        """
        Return Cairo expression which will bind source code surfacing iterator reference.
        """

    @abstractmethod
    def increment_iterator(self, *iters: ExprIdentifier) -> Tuple[CodeBlock, List[Expression]]:
        """
        Provide Cairo code which increments iterator variables.
        """

    @staticmethod
    def from_in_clause(clause: ForClauseIn) -> "GeneratorLowering":
        # We are importing locally to prevent import cycles
        # from starkware.cairo.lang.compiler.preprocessor.for_loop.range_generator import (
        #     RangeGeneratorLowering,
        # )
        # from starkware.cairo.lang.compiler.preprocessor.for_loop.slice_generator import (
        #     SliceGeneratorLowering,
        # )

        generator = clause.generator
        if isinstance(generator, ForGeneratorRange):
            # return RangeGeneratorLowering(generator)
            return NotImplemented
        elif isinstance(generator, ForGeneratorSlice):
            # return SliceGeneratorLowering(generator)
            return NotImplemented
        else:
            raise NotImplementedError(
                f"Lowering '{generator.func_ident.name}' generator is not implemented yet."
            )
