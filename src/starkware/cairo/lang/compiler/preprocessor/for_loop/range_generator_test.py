from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import verify_exception


def test_range_without_arguments():
    verify_exception(
        """
func main():
    for i in range():
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Range generator expects at least the stop argument.
    for i in range():
             ^*****^
""",
        exc_type=ForLoopLoweringError,
    )


def test_range_with_too_many_arguments():
    verify_exception(
        """
func main():
    for i in range(1, 2, 3, 4, 5):
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Too many arguments passed to range generator.
    for i in range(1, 2, 3, 4, 5):
                            ^**^
        """,
        exc_type=ForLoopLoweringError,
    )


def test_range_with_keyword_arguments():
    verify_exception(
        """
func main():
    for i in range(1, 2, step=4):
        [ap] = 2; ap++
    end
end
""",
        """
file:?:?: Keyword arguments are not supported here yet.
    for i in range(1, 2, step=4):
                         ^****^
        """,
        exc_type=ForLoopLoweringError,
    )
