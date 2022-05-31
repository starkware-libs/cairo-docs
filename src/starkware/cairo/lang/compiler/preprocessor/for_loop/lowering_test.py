from starkware.cairo.lang.compiler.preprocessor.for_loop.lowering_test_utils import verify_exception


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
