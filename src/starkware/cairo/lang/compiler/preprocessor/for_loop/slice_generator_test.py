from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import verify_exception


def test_slice_without_arguments():
    verify_exception(
        "for i in slice():\n    [ap] = 2; ap++\nend",
        """
file:?:?: Slice generator expects at least 'array' and 'number' arguments.
for i in slice():
         ^*****^
""",
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_one_argument():
    verify_exception(
        "for i in slice(array):\n    [ap] = 2; ap++\nend",
        """
file:?:?: Slice generator expects at least 'array' and 'number' arguments.
for i in slice(array):
         ^**********^
""",
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_too_many_arguments():
    verify_exception(
        "for i in slice(1, 2, 3, 4, 5):\n    [ap] = 2; ap++\nend",
        """
file:?:?: Too many arguments passed to slice generator.
for i in slice(1, 2, 3, 4, 5):
                        ^**^
        """,
        exc_type=ForLoopLoweringError,
    )


def test_slice_with_keyword_arguments():
    verify_exception(
        "for i in slice(array, 2, size=4):\n    [ap] = 2; ap++\nend",
        """
file:?:?: Keyword arguments are not supported here yet.
for i in slice(array, 2, size=4):
                         ^****^
        """,
        exc_type=ForLoopLoweringError,
    )
