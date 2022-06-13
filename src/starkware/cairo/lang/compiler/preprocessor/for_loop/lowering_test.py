import pytest

from starkware.cairo.lang.compiler.preprocessor.for_loop.lowering_test_utils import (
    lower_and_format,
    verify_exception,
)


def test_for_outside_function():
    verify_exception(
        """
for i in range(10):
    let x = 5
end
func main():
    ret
end
""",
        """
file:?:?: For loops are unsupported outside functions.
for i in range(10):
^*^
""",
    )


@pytest.mark.skip
def test_for_unused_iterator():
    code = """
func main():
    for _i in range(7, 24, 2):
        [ap] = 42; ap++
        [ap] = 43; ap++
    end
    [ap] = 1234; ap++
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    $func0($var1=7)
    [ap] = 1234; ap++
    ret
end
func $func0($var1 : felt):
    alloc_locals
    if $var1 == 24:
        return ()
    end
    let _i = $var1
    [ap] = 42; ap++
    [ap] = 43; ap++
    return $func0($var1=$var1 + 2)
end
"""
    )


@pytest.mark.skip
def test_for_range_backward():
    code = """
func main():
    for _i in range(24, -7, -2):
        [ap] = 42; ap++
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    $func0($var1=24)
    ret
end
func $func0($var1 : felt):
    alloc_locals
    if $var1 == -7:
        return ()
    end
    let _i = $var1
    [ap] = 42; ap++
    return $func0($var1=$var1 + (-2))
end
"""
    )


@pytest.mark.skip
def test_for_typed_iterator():
    code = """
func main():
    for i : felt* in range(5):
        assert [i] = 456
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    $func0($var1=0)
    ret
end
func $func0($var1 : felt):
    alloc_locals
    if $var1 == 5:
        return ()
    end
    let i : felt* = cast($var1, felt*)
    assert [i] = 456
    return $func0($var1=$var1 + 1)
end
"""
    )


@pytest.mark.skip
def test_for_slice_over_felts():
    code = """
func main():
    let array : felt* = alloc()
    for i : felt* in slice(array, 123):
        assert [i] = 456
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let array : felt* = alloc()
    $func0($var1=array, $var2=array + 123 * 1)
    ret
end
func $func0($var1 : felt*, $var2 : felt*):
    alloc_locals
    if $var1 == $var2:
        return ()
    end
    let i : felt* = cast($var1, felt*)
    assert [i] = 456
    return $func0($var1=$var1 + 1, $var2=$var2)
end
"""
    )


@pytest.mark.skip
def test_for_slice_over_structs():
    code = """
func main():
    let array : Point* = alloc()
    for i : Point* in slice(array, 123, Point.SIZE):
        assert i.x = 456
        assert i.y = 567
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    let array : Point* = alloc()
    $func0($var1=array, $var2=array + 123 * Point.SIZE)
    ret
end
func $func0($var1 : felt*, $var2 : felt*):
    alloc_locals
    if $var1 == $var2:
        return ()
    end
    let i : Point* = cast($var1, Point*)
    assert i.x = 456
    assert i.y = 567
    return $func0($var1=$var1 + Point.SIZE, $var2=$var2)
end
"""
    )


@pytest.mark.skip
def test_for_reference_body_vars():
    code = """
func main():
    alloc_locals
    local x = 10
    local y = 11
    for i in range(5), with(x, y):
        tempvar f = x * y + 456
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    alloc_locals
    local x = 10
    local y = 11
    $func0($var1=0, x=x, y=y)
    ret
end
func $func0($var1 : felt, x, y):
    alloc_locals
    if $var1 == 5:
        return ()
    end
    let i = $var1
    tempvar f = x * y + 456
    return $func0($var1=$var1 + 1, x=x, y=y)
end
"""
    )


@pytest.mark.skip
def test_for_access_implicit_arguments():
    code = """
func foo{implicit_ptr : felt*}():
    for i in range(5):
        write(i)
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func foo{implicit_ptr : felt*}():
    $func0($var1=0)
    ret
end
func $func0{implicit_ptr : felt*}($var1 : felt):
    alloc_locals
    if $var1 == 5:
        return ()
    end
    let i = $var1
    write(i)
    return $func0($var1=$var1 + 1)
end
"""
    )


@pytest.mark.skip
def test_nested_for():
    code = """
func main():
    for i in range(100):
        let z = i
        for j in range(101):
            let y = j
            for k in range(102):
                let x = k
            end
        end
    end
    ret
end
"""
    assert (
        lower_and_format(code)
        == """\
func main():
    $func0($var1=0)
    ret
end
func $func0($var1 : felt):
    alloc_locals
    if $var1 == 100:
        return ()
    end
    let i = $var1
    let z = i
    $func2($var3=0)
    return $func0($var1=$var1 + 1)
end
func $func2($var3 : felt):
    alloc_locals
    if $var3 == 101:
        return ()
    end
    let j = $var3
    let y = j
    $func4($var5=0)
    return $func2($var3=$var3 + 1)
end
func $func4($var5 : felt):
    alloc_locals
    if $var5 == 102:
        return ()
    end
    let k = $var5
    let x = k
    return $func4($var5=$var5 + 1)
end
"""
    )


def test_alloc_locals_in_for_loop_body():
    verify_exception(
        """
func main():
    for i in range(5):
        alloc_locals
        local f = i
    end
    ret
end
""",
        """
file:?:?: alloc_locals is not allowed in the body of a for loop.
        alloc_locals
        ^**********^
""",
    )
