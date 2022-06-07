from starkware.cairo.lang.compiler.preprocessor.if_statements.lowering_test_utils import (
    lower_and_format,
)


def test_lowers_single_and_without_else():
    code = """
func main():
    let a = 10
    let b = 12
    if a == 10 and b == 12:
        let x = a + b
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let a = 10
    let b = 12

    $lbl0:
    jmp $lbl3 if a - 10 != 0

    $lbl1:
    jmp $lbl3 if b - 12 != 0

    $lbl2:
    let x = a + b

    $lbl3:
    ret
end
"""
    )


def test_lowers_nested_and_without_else():
    code = """
func main():
    let a = 10
    let b = 12
    let c = 14
    if a == 10 and b == 12 and c == 14:
        let x = a + b + c
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let a = 10
    let b = 12
    let c = 14

    $lbl0:
    jmp $lbl4 if a - 10 != 0

    $lbl1:
    jmp $lbl4 if b - 12 != 0

    $lbl2:
    jmp $lbl4 if c - 14 != 0

    $lbl3:
    let x = a + b + c

    $lbl4:
    ret
end
"""
    )


def test_lowers_else_block():
    code = """
func main():
    let a = 10
    let b = 12
    if a == 10 and b != 12:
        let x = a + b
    else:
        let x = a - b
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let a = 10
    let b = 12

    $lbl0:
    jmp $lbl2 if a - 10 != 0

    $lbl1:
    jmp $lbl3 if b - 12 != 0

    $lbl2:
    let x = a - b
    jmp $lbl4

    $lbl3:
    let x = a + b

    $lbl4:
    ret
end
"""
    )


def test_nested():
    code = """
func main():
    let a = 10
    let b = 12
    if a == 10 and b != 12:
        if a != 20 and b == 21: 
            let x = a + b
        else:
            let x = 2 * a
        end
    else:
        if b == 31 and a != 32:
            let x = a - b
        else:
            let x = 2 * b
        end
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let a = 10
    let b = 12

    $lbl0:
    jmp $lbl2 if a - 10 != 0

    $lbl1:
    jmp $lbl3 if b - 12 != 0

    $lbl2:

    $lbl10:
    jmp $lbl12 if b - 31 != 0

    $lbl11:
    jmp $lbl13 if a - 32 != 0

    $lbl12:
    let x = 2 * b
    jmp $lbl14

    $lbl13:
    let x = a - b

    $lbl14:
    jmp $lbl4

    $lbl3:

    $lbl5:
    jmp $lbl6 if a - 20 != 0
    jmp $lbl8

    $lbl6:
    jmp $lbl8 if b - 21 != 0

    $lbl7:
    let x = a + b
    jmp $lbl9

    $lbl8:
    let x = 2 * a

    $lbl9:

    $lbl4:
    ret
end
"""
    )
