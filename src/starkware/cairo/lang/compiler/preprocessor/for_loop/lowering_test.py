from starkware.cairo.lang.compiler.preprocessor.for_loop.lowering_test_utils import lower_and_format


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
    $0($1=7)
    [ap] = 1234; ap++
    ret
end
func $0($1 : felt):
    if $1 == 24:
        return ()
    else:
        let _i = $1
        [ap] = 42; ap++
        [ap] = 43; ap++
        return $0($1=$1 + 2)
    end
end
"""
    )


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
    $0($1=24)
    ret
end
func $0($1 : felt):
    if $1 == -7:
        return ()
    else:
        let _i = $1
        [ap] = 42; ap++
        return $0($1=$1 + (-2))
    end
end
"""
    )


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
    $0($1=0)
    ret
end
func $0($1 : felt):
    if $1 == 5:
        return ()
    else:
        let i : felt* = cast($1, felt*)
        assert [i] = 456
        return $0($1=$1 + 1)
    end
end
"""
    )


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
    $0($1=array, $2=array + 123 * 1)
    ret
end
func $0($1 : felt*, $2 : felt*):
    if $1 == $2:
        return ()
    else:
        let i : felt* = cast($1, felt*)
        assert [i] = 456
        return $0($1=$1 + 1, $2=$2)
    end
end
"""
    )


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
    $0($1=array, $2=array + 123 * Point.SIZE)
    ret
end
func $0($1 : felt*, $2 : felt*):
    if $1 == $2:
        return ()
    else:
        let i : Point* = cast($1, Point*)
        assert i.x = 456
        assert i.y = 567
        return $0($1=$1 + Point.SIZE, $2=$2)
    end
end
"""
    )


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
    $0($1=0)
    ret
end
func $0{implicit_ptr : felt*}($1 : felt):
    if $1 == 5:
        return ()
    else:
        let i = $1
        write(i)
        return $0($1=$1 + 1)
    end
end
"""
    )


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
    $0($1=0)
    ret
end
func $0($1 : felt):
    if $1 == 100:
        return ()
    else:
        let i = $1
        let z = i
        $2($3=0)
        return $0($1=$1 + 1)
    end
end
func $2($3 : felt):
    if $3 == 101:
        return ()
    else:
        let j = $3
        let y = j
        $4($5=0)
        return $2($3=$3 + 1)
    end
end
func $4($5 : felt):
    if $5 == 102:
        return ()
    else:
        let k = $5
        let x = k
        return $4($5=$5 + 1)
    end
end
"""
    )
