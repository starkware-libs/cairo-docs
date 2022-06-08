from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import verify_exception


def test_slice_without_arguments():
    verify_exception(
        """
func main():
    for i in slice():
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Slice generator expects at least 'array' and 'number' arguments.
    for i in slice():
             ^*****^
""",
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_one_argument():
    verify_exception(
        """
func main():
    for i in slice(array):
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Slice generator expects at least 'array' and 'number' arguments.
    for i in slice(array):
             ^**********^
""",
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_too_many_arguments():
    verify_exception(
        """
func main():
    for i in slice(1, 2, 3, 4, 5):
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Too many arguments passed to slice generator.
    for i in slice(1, 2, 3, 4, 5):
                            ^**^
        """,
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_keyword_arguments():
    verify_exception(
        """
func main():
    for i in slice(array, 2, size=4):
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Keyword arguments are not supported here yet.
    for i in slice(array, 2, size=4):
                             ^****^
        """,
        exc_type=ForLoopLoweringError,
    )
