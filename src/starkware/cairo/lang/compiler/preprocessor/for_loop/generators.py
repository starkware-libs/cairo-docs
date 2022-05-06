from abc import ABC, abstractmethod
from typing import Tuple

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
    def iterator_type(self) -> CairoType:
        """
        Provide Cairo type of iterator values returned by this generator.
        """

    @abstractmethod
    def init_envelope_iterator(self) -> Tuple[CodeBlock, Expression]:
        """
        Provide Cairo code which initializes the iterator variable.
        """

    @abstractmethod
    def condition(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, BoolExpr]:
        """
        Provide Cairo code which checks if iteration reaches end.
        """

    @abstractmethod
    def increment_iterator(self, iter_expr: ExprIdentifier) -> Tuple[CodeBlock, Expression]:
        """
        Provide Cairo code which increments iterator variable.
        """

    @staticmethod
    def from_in_clause(clause: ForClauseIn) -> "GeneratorLowering":
        # We are importing locally to prevent import cycles
        from starkware.cairo.lang.compiler.preprocessor.for_loop.range_generator import (
            RangeGeneratorLowering,
        )
        from starkware.cairo.lang.compiler.preprocessor.for_loop.slice_generator import (
            SliceGeneratorLowering,
        )

        generator = clause.generator
        if isinstance(generator, ForGeneratorRange):
            return RangeGeneratorLowering(generator)
        elif isinstance(generator, ForGeneratorSlice):
            return SliceGeneratorLowering(generator)
        else:
            raise NotImplementedError(
                f"Lowering '{generator.func_ident.name}' generator is not implemented yet."
            )
