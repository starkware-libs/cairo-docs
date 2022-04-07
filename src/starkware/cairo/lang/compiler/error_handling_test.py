import pytest

from starkware.cairo.lang.compiler.error_handling import InputFile, Location, LocationError


def test_location_error():
    content = """\
First line,
second line.
"""
    location = Location(
        start_line=2,
        start_col=8,
        end_line=2,
        end_col=12,
        input_file=InputFile(filename="file.cairo", content=content),
    )

    expected_message = "file.cairo:2:8: Error message."
    expected_message_with_content = f"""\
{expected_message}
second line.
       ^**^\
"""
    assert location.to_string("Error message.") == expected_message
    assert str(location) == "file.cairo:2:8"
    assert location.to_string_with_content("Error message.") == expected_message_with_content
    assert str(LocationError("Error message.", location=location)) == expected_message_with_content

    err2 = LocationError(message="Error message.", location=None)
    err2.notes.append("note1")
    err2.notes.append("note2")
    assert (
        str(err2)
        == """\
Error message.
note1
note2"""
    )


def test_missing_source_file():
    location = Location(
        start_line=2,
        start_col=8,
        end_line=2,
        end_col=12,
        input_file=InputFile(filename="missing_file.cairo", content=None),
    )

    expected_message = "missing_file.cairo:2:8: Error message."
    assert location.to_string_with_content("Error message.") == expected_message


def test_location_span():
    file = InputFile(filename="file.cairo", content="")

    a = Location(1, 2, 3, 4, file)
    b = Location(5, 6, 7, 8, file)

    assert a.span(b) == Location(1, 2, 7, 8, file)
    assert a.span(b) == b.span(a)


def test_location_span_contained():
    file = InputFile(filename="file.cairo", content="")

    a = Location(1, 2, 10, 11, file)
    b = Location(2, 3, 8, 9, file)

    assert a.span(b) == a
    assert b.span(a) == a


def test_location_span_preserves_parent_location_if_same():
    file = InputFile(filename="file.cairo", content="")

    a = Location(1, 2, 3, 4, file, parent_location=(Location(1, 1, 1, 10, file), "a"))
    b = Location(5, 6, 7, 8, file, parent_location=(Location(1, 1, 1, 10, file), "a"))

    assert a.span(b) == Location(
        1, 2, 7, 8, file, parent_location=(Location(1, 1, 1, 10, file), "a")
    )


def test_location_span_raises_if_input_files_differ():
    file1 = InputFile(filename="file1.cairo", content="")
    file2 = InputFile(filename="file2.cairo", content="")

    a = Location(1, 2, 3, 4, file1)
    b = Location(5, 6, 7, 8, file2)

    with pytest.raises(ValueError):
        a.span(b)


def test_location_span_raises_if_parent_location_differs():
    file = InputFile(filename="file.cairo", content="")

    a = Location(1, 2, 3, 4, file, parent_location=(Location(1, 1, 1, 10, file), "a"))
    b = Location(5, 6, 7, 8, file, parent_location=(Location(2, 2, 2, 20, file), "b"))

    with pytest.raises(ValueError):
        a.span(b)
