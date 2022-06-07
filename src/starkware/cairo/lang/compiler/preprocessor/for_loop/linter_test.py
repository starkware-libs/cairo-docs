from starkware.cairo.lang.compiler.preprocessor.for_loop.lowering_test_utils import verify_exception


def test_alloc_locals():
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


def test_return():
    verify_exception(
        """
func main():
    for i in range(5):
        local f = i
        return (f)
    end
    ret
end
""",
        """
file:?:?: return is not allowed in for loop body.
        return (f)
        ^********^
""",
    )


def test_ret():
    verify_exception(
        """
func main():
    for i in range(5):
        ret
    end
    ret
end
""",
        """
file:?:?: ret is not allowed in for loop body.
        ret
        ^*^
""",
    )


def test_tail_call():
    verify_exception(
        """
func main():
    for i in range(5):
        local f = i
        return helper(f)
    end
    ret
end
""",
        """
file:?:?: return is not allowed in for loop body.
        return helper(f)
        ^**************^
""",
    )


def test_return_in_if_body():
    verify_exception(
        """
func main():
    for i in range(5):
        local f = i
        if i == 2:
            return (f)
        end
    end
    ret
end
""",
        """
file:?:?: return is not allowed in for loop body.
            return (f)
            ^********^
""",
    )
