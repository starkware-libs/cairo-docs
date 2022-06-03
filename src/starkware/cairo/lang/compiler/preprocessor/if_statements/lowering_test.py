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
    jmp $lbl0 if a - 10 != 0
    jmp $lbl0 if b - 12 != 0
    let x = a + b

    $lbl0:
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
    jmp $lbl0 if a - 10 != 0
    jmp $lbl0 if b - 12 != 0
    jmp $lbl0 if c - 14 != 0
    let x = a + b + c

    $lbl0:
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
    jmp $lbl0 if a - 10 != 0
    jmp $lbl1 if b - 12 != 0

    $lbl0:
    let x = a - b
    jmp $lbl2

    $lbl1:
    let x = a + b

    $lbl2:
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
    jmp $lbl0 if a - 10 != 0
    jmp $lbl1 if b - 12 != 0

    $lbl0:
    jmp $lbl6 if b - 31 != 0
    jmp $lbl7 if a - 32 != 0

    $lbl6:
    let x = 2 * b
    jmp $lbl8

    $lbl7:
    let x = a - b

    $lbl8:
    jmp $lbl2

    $lbl1:
    jmp $lbl3 if a - 20 != 0
    jmp $lbl4

    $lbl3:
    jmp $lbl4 if b - 21 != 0
    let x = a + b
    jmp $lbl5

    $lbl4:
    let x = 2 * a

    $lbl5:

    $lbl2:
    ret
end
"""
    )
