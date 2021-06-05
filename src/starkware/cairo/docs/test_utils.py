import dataclasses
from collections import defaultdict
from enum import Enum, auto
from typing import Dict

import isort

from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementDirective, CodeElementEmptyLine, CodeElementImport, CommentedCodeElement)
from starkware.cairo.lang.compiler.parser import parse_file


def reorganize_code(code: str) -> str:
    """
    Moves directives (e.g., %builtins) and import statements to the top of the code and sorts the
    imports.
    """

    cairo_file = parse_file(code=code, filename='')

    class CodeElementType(Enum):
        DIRECTIVE = 0
        IMPORT = auto()
        OTHER = auto()

    def element_type(code_element: CommentedCodeElement):
        if isinstance(code_element.code_elm, CodeElementDirective):
            return CodeElementType.DIRECTIVE
        elif isinstance(code_element.code_elm, CodeElementImport):
            return CodeElementType.IMPORT
        else:
            return CodeElementType.OTHER

    code_element_by_group: Dict[CodeElementType, CommentedCodeElement] = defaultdict(list)
    for code_element in cairo_file.code_block.code_elements:
        code_element_by_group[element_type(code_element)].append(code_element)
    empty_line = CommentedCodeElement(code_elm=CodeElementEmptyLine(), comment=None)
    code_elements = [
        *code_element_by_group[CodeElementType.DIRECTIVE],
        empty_line,
        *code_element_by_group[CodeElementType.IMPORT],
        empty_line,
        *code_element_by_group[CodeElementType.OTHER]
    ]
    cairo_file = dataclasses.replace(
        cairo_file,
        code_block=dataclasses.replace(
            cairo_file.code_block,
            code_elements=code_elements,
        ),
    )

    code = cairo_file.format()
    code = isort.SortImports(file_contents=code, lines_after_imports=1).output
    return code
