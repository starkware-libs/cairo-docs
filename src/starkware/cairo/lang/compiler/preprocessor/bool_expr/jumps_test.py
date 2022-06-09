from starkware.cairo.lang.compiler.ast.bool_expr import BoolAndExpr, BoolEqExpr, BoolOrExpr
from starkware.cairo.lang.compiler.preprocessor.bool_expr.jumps import (
    BoolExprId,
    EXIT_ID,
    Exit,
    FALSE_ID,
    JumpTable,
    JumpToLabelDescriptor,
    TRUE_ID,
    Terminal,
    convert_bool_expr_to_jumps,
)


def test_convert_bool_expr_to_jumps():
    # (a and !b) or (!c and d)
    a = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    b = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    c = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    d = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    expr = BoolOrExpr(
        a=BoolAndExpr(
            a=a,
            b=b,
        ),
        b=BoolAndExpr(
            a=c,
            b=d,
        ),
    )

    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=True) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=a,
                on_true=BoolExprId(1),
                on_false=BoolExprId(2),
            ),
            BoolExprId(1): JumpToLabelDescriptor(
                bool_expr=b,
                on_true=BoolExprId(2),
                on_false=TRUE_ID,
            ),
            BoolExprId(2): JumpToLabelDescriptor(
                bool_expr=c,
                on_true=FALSE_ID,
                on_false=BoolExprId(3),
            ),
            BoolExprId(3): JumpToLabelDescriptor(
                bool_expr=d,
                on_true=TRUE_ID,
                on_false=FALSE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            FALSE_ID: Terminal(case=False, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_bool_expr_to_jumps_without_else():
    # (a and !b) or (!c and d)
    a = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    b = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    c = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    d = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    expr = BoolOrExpr(
        a=BoolAndExpr(
            a=a,
            b=b,
        ),
        b=BoolAndExpr(
            a=c,
            b=d,
        ),
    )

    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=False) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=a,
                on_true=BoolExprId(1),
                on_false=BoolExprId(2),
            ),
            BoolExprId(1): JumpToLabelDescriptor(
                bool_expr=b,
                on_true=BoolExprId(2),
                on_false=TRUE_ID,
            ),
            BoolExprId(2): JumpToLabelDescriptor(
                bool_expr=c,
                on_true=EXIT_ID,
                on_false=BoolExprId(3),
            ),
            BoolExprId(3): JumpToLabelDescriptor(
                bool_expr=d,
                on_true=TRUE_ID,
                on_false=EXIT_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_eq_to_jump():
    expr = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=True) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=expr,
                on_true=TRUE_ID,
                on_false=FALSE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            FALSE_ID: Terminal(case=False, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_neq_to_jump():
    expr = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=True) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=expr,
                on_true=FALSE_ID,
                on_false=TRUE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            FALSE_ID: Terminal(case=False, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_and_to_jump():
    # a and !b
    a = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    b = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    expr = BoolAndExpr(a=a, b=b)

    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=True) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=a,
                on_true=BoolExprId(1),
                on_false=FALSE_ID,
            ),
            BoolExprId(1): JumpToLabelDescriptor(
                bool_expr=b,
                on_true=FALSE_ID,
                on_false=TRUE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            FALSE_ID: Terminal(case=False, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_and_to_jump_without_else():
    # a and !b
    a = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    b = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    expr = BoolAndExpr(a=a, b=b)

    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=False) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=a,
                on_true=BoolExprId(1),
                on_false=EXIT_ID,
            ),
            BoolExprId(1): JumpToLabelDescriptor(
                bool_expr=b,
                on_true=EXIT_ID,
                on_false=TRUE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )


def test_convert_or_to_jump():
    # a or !b
    a = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=True)
    b = BoolEqExpr(a=NotImplemented, b=NotImplemented, eq=False)
    expr = BoolOrExpr(a=a, b=b)

    assert convert_bool_expr_to_jumps(expr=expr, has_false_case=True) == JumpTable(
        {
            BoolExprId(0): JumpToLabelDescriptor(
                bool_expr=a,
                on_true=TRUE_ID,
                on_false=BoolExprId(1),
            ),
            BoolExprId(1): JumpToLabelDescriptor(
                bool_expr=b,
                on_true=FALSE_ID,
                on_false=TRUE_ID,
            ),
            TRUE_ID: Terminal(case=True, exit=EXIT_ID),
            FALSE_ID: Terminal(case=False, exit=EXIT_ID),
            EXIT_ID: Exit(),
        }
    )
