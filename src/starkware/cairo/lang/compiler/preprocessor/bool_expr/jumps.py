import dataclasses
from abc import ABC
from typing import NewType, Optional, Union, Dict, OrderedDict

from starkware.cairo.lang.compiler.ast.bool_expr import (
    BoolAndExpr,
    BoolEqExpr,
    BoolExpr,
    BoolOrExpr,
)
from starkware.cairo.lang.compiler.ast.visitor import Visitor

BoolExprId = NewType("BoolExprId", Union[int, str])

TRUE_ID = BoolExprId("T")
FALSE_ID = BoolExprId("F")
EXIT_ID = BoolExprId("X")


@dataclasses.dataclass
class JumpTableItem(ABC):
    pass


@dataclasses.dataclass
class JumpToLabelDescriptor(JumpTableItem):
    """
    A value describing the parameters of ``jmp label if expr != 0`` (``JumpToLabelInstruction``)
    instruction which will realise given ``BoolEqExpr`` being part of more complex ``BoolExpr``.
    """

    bool_expr: BoolEqExpr
    on_true: Optional[BoolExprId]
    on_false: BoolExprId


@dataclasses.dataclass
class Terminal(JumpTableItem):
    """
    Placeholder value reflecting location of if's ``main`` (``case=True``)
    or ``else`` (``case=False``) code blocks.
    """

    case: bool
    exit: Optional[BoolExprId]


@dataclasses.dataclass
class Exit(JumpTableItem):
    """
    Placeholder value reflecting end of the statement.

    It should compile to a label after code generated in lowering.
    """


class JumpTable(OrderedDict[BoolExprId, JumpTableItem]):
    """
    A single conditional jump instruction can be treated as following graph node, with one input
    and two outputs::

                                  ┌──► [ on_true ]
        [ input ] ──► condition ──┤
                                  └──► [ on_false ]

    Compiled, this would build a following Cairo pseudocode::

        input:
            jmp on_false if condition != 0
        on_true:

    A ``JumpTable`` is a graph of such nodes, layout out as an ordered dictionary, where edges
    are represented as keys of the dictionary.

    Jump table also includes two extra nodes, called ``Terminal``s. They represent the ``main``
    and ``else`` code blocks of processed ``CodeElementIf``, and their purpose is to denote the
    order in which these code blocks should be emitted. In negations usually, some jumps can be
    avoided if the ``else`` block is before the ``main`` one.

    Finally, always at the end, there should be an ``Exit`` node which represents end of the
    statement. All terminals should lead to exit.

    Order of keys reflects order of execution.

    Keys are opaque and are guaranteed to be stable for many evaluations of same boolean expression,
    in order to allow jump tables to be compared for equality.
    Keys are not guaranteed to be sequential nor consecutive nor start/end with defined value.
    """


def convert_bool_expr_to_jumps(expr: BoolExpr, has_false_case: bool) -> JumpTable:
    """
    Converts a ``BoolExpr`` given as ``CodeElementIf``'s condition into a series of
    ``JumpToLabelInstruction``'s.

    This function implements only the algorithm. It does not build any code elements,
    instead it operates on abstract items subclassing from ``JumpTableItem``

    ## Algorithm

    The conversion algorithm consists of 3 parts:

    1. Assign unique numeric value (``BoolExprId``) to each leaf (``BoolEqExpr``) of
       input ``BoolExpr``. These values are used as pointers in emitted ``JumpTable``.
    2. Walk entire expression tree and emit ``JumpToLabelDescriptor``s, wiring them together
       in such a way that the jumps will emulate boolean operations, assuming lazy evaluation.

       Refer to the source code of the ``visit_`` methods of ``_JumpTableBuilder`` to see how
       particular connections are laid out for each boolean expression type.
    3. Apply some optimizations which will lead to less amount of jump instructions emitted.
    """

    expr_index_builder = _ExprIndexBuilder()
    expr_index_builder.visit(expr)
    expr_index = expr_index_builder.index

    builder = _JumpTableBuilder(expr_index=expr_index, has_false_case=has_false_case)
    builder.visit_terminal(expr)
    jump_table = builder.jump_table

    return jump_table


_ExprIndex = Dict[BoolExprId, BoolExpr]


class _ExprIndexBuilder(Visitor):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.index: _ExprIndex = {}

    def visit_BoolEqExpr(self, expr: BoolEqExpr):
        self.index[self.counter] = expr
        self.counter += 1

    def visit_BoolAndExpr(self, expr: BoolAndExpr):
        self.visit(expr.a)
        self.visit(expr.b)

    def visit_BoolOrExpr(self, expr: BoolAndExpr):
        self.visit(expr.a)
        self.visit(expr.b)


class _ReverseExprIndex:
    def __init__(self, expr_index: _ExprIndex):
        self.reverse_expr_index = {id(v): k for k, v in expr_index.items()}

    def __getitem__(self, expr: BoolExpr) -> BoolExprId:
        return self.reverse_expr_index[id(expr)]


class _JumpTableBuilder:
    def __init__(self, expr_index: _ExprIndex, has_false_case: bool):
        self.jump_table = JumpTable()
        self.has_false_case = has_false_case
        self.reverse_expr_index = _ReverseExprIndex(expr_index)

    def visit_terminal(self, expr: BoolExpr):
        self.visit(
            expr=expr,
            on_true=TRUE_ID,
            on_false=FALSE_ID if self.has_false_case else EXIT_ID,
        )

        self.jump_table[TRUE_ID] = Terminal(case=True, exit=EXIT_ID)

        if self.has_false_case:
            self.jump_table[FALSE_ID] = Terminal(case=False, exit=EXIT_ID)

        self.jump_table[EXIT_ID] = Exit()

    def visit(self, expr: BoolExpr, on_true: BoolExprId, on_false: BoolExprId):
        func = getattr(self, f"visit_{type(expr).__name__}")
        return func(expr=expr, on_true=on_true, on_false=on_false)

    def visit_BoolEqExpr(self, expr: BoolEqExpr, on_true: BoolExprId, on_false: BoolExprId):
        if expr.eq:
            branch = JumpToLabelDescriptor(bool_expr=expr, on_true=on_true, on_false=on_false)
        else:
            branch = JumpToLabelDescriptor(bool_expr=expr, on_true=on_false, on_false=on_true)

        self.jump_table[self.reverse_expr_index[expr]] = branch

    def visit_BoolAndExpr(self, expr: BoolAndExpr, on_true: BoolExprId, on_false: BoolExprId):
        b_expr_id = self.first_leaf_id_of(expr.b)

        self.visit(expr=expr.a, on_true=b_expr_id, on_false=on_false)
        self.visit(expr=expr.b, on_true=on_true, on_false=on_false)

    def visit_BoolOrExpr(self, expr: BoolOrExpr, on_true: BoolExprId, on_false: BoolExprId):
        b_expr_id = self.first_leaf_id_of(expr.b)

        self.visit(expr=expr.a, on_true=on_true, on_false=b_expr_id)
        self.visit(expr=expr.b, on_true=on_true, on_false=on_false)

    def first_leaf_id_of(self, expr: BoolExpr) -> BoolExprId:
        return self.reverse_expr_index[expr.first_bool_leaf()]
