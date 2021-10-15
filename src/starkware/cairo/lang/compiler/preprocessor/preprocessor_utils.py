import hashlib
from typing import Optional

from starkware.cairo.lang.compiler.ast.code_elements import CodeBlock, CodeElementEmptyLine
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.error_handling import Location, ParentLocation
from starkware.cairo.lang.compiler.parser import ParserContext, parse
from starkware.cairo.lang.compiler.preprocessor.preprocessor_error import PreprocessorError


def assert_no_modifier(typed_identifier: TypedIdentifier):
    """
    Throws a PreprocessorError if typed_identifier has a modifier.
    """
    if typed_identifier.modifier is not None:
        raise PreprocessorError(
            f"Unexpected modifier '{typed_identifier.modifier.format()}'.",
            location=typed_identifier.modifier.location)


def verify_empty_code_block(
        code_block: CodeBlock, error_message: str, default_location: Optional[Location]):
    """
    Verifies that the given code_block is empty (except for empty lines) and raises an exception
    otherwise.
    """
    for commented_code_elm in code_block.code_elements:
        code_elm = commented_code_elm.code_elm
        if not isinstance(code_elm, CodeElementEmptyLine):
            if hasattr(code_elm, 'location'):
                location = code_elm.location  # type: ignore
            elif commented_code_elm.location is not None:
                location = commented_code_elm.location
            else:
                location = default_location
            raise PreprocessorError(error_message, location=location)


def autogen_parse_code_block(
    path: str, code: str, parent_location: Optional[ParentLocation]
) -> CodeBlock:
    """
    Parses the given code as CodeBlock.
    Can be used for auto-generation of code during compilation.
    """
    code_hash = hashlib.sha256(code.encode()).hexdigest()
    filename = f'{path}/{code_hash}.cairo'
    return parse(
        filename=filename,
        code=code,
        code_type='code_block',
        expected_type=CodeBlock,
        parser_context=ParserContext(parent_location=parent_location),
    )
