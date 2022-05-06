from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import verify_exception


def test_range_without_arguments():
    verify_exception(
        "for i in range():\n    [ap] = 2; ap++\nend",
        """
file:?:?: Range generator excepts at least the stop argument.
for i in range():
         ^*****^
""",
        exc_type=ForLoopLoweringError,
    )


def test_range_with_too_many_arguments():
    verify_exception(
        "for i in range(1, 2, 3, 4, 5):\n    [ap] = 2; ap++\nend",
        """
file:?:?: Too many arguments passed to range generator.
for i in range(1, 2, 3, 4, 5):
                        ^**^
        """,
        exc_type=ForLoopLoweringError,
    )


def test_range_with_keyword_arguments():
    verify_exception(
        "for i in range(1, 2, step=4):\n    [ap] = 2; ap++\nend",
        """
file:?:?: Keyword arguments are not supported here yet.
for i in range(1, 2, step=4):
                     ^****^
        """,
        exc_type=ForLoopLoweringError,
    )
