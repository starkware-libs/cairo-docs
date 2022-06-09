from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import verify_exception


def test_for_without_clauses():
    verify_exception(
        """
func main():
    for:
        f()
    end
end
""",
        """
file:?:?: For loop requires one 'in' clause.
    for:
    ^*^
""",
        exc_type=ForLoopLoweringError,
    )


def test_for_many_in_clauses():
    verify_exception(
        """
func main():
    for _ in range(1), _ in range(2), _ in range(3):
        f()
    end
end
    """,
        """
file:?:?: Multiple 'in' clauses in for loops are not supported.
    for _ in range(1), _ in range(2), _ in range(3):
                       ^**************************^
""",
        exc_type=ForLoopLoweringError,
    )
