import json
import os
import re
import sys
import traceback
from typing import Dict, Iterable, Sequence, Union

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.builders import Builder

from starkware.cairo.lang.compiler.ast.formatting_utils import set_max_line_length
from starkware.cairo.lang.compiler.parser import parse_file

MAX_LINE_LENGTH = 65
DOCS_TEST_FILTER_ENV_VAR = "DOCS_TEST_FILTER"


class TestedCodeDirective(Directive):
    """
    Stores the code for testing, in addition to adding a paragraph to the document.
    Directive arguments: language, name - where the name is used to access this code in tests.

    Directive usage example:
    .. tested-code:: python hello_world

      print('Hello world')

    This will create a code paragraph in the documentation and will store the text of that paragraph
    (the string "print('Hello world')" in the example above) for tests which appears later using
    the test directive.
    """

    has_content = True
    required_arguments = 2

    def run(self):
        language, code_name = self.arguments
        code = "\n".join(self.content)

        node = nodes.literal_block(code, code)
        node["language"] = language
        node["testing_tested_code_name"] = code_name

        return [node]


class TestDirective(Directive):
    """
    Runs a given test when using the testcode builder (TestCodeBuilder).
    The test will not appear in the documentation output.

    Directive usage example:

    .. test::
      assert 'Hello world' in codes['hello']

    Codes which were stored using the tested-code directive are accessible using the 'codes'
    dictionary.

    Use the DOCS_TEST_FILTER environment variable to restrict the *.rst files being tested.
    For example, use
      DOCS_TEST_FILTER=builtins scripts/burn.py --target cairo_docs_test
    to run all the tests in *.rst files that contain the word 'builtins'.
    """

    has_content = True

    def run(self):
        test_code = "\n".join(self.content)

        node = nodes.comment(test_code, test_code)
        node["testing_test"] = True

        return [node]


class TestCodeBuilder(Builder):
    """
    A builder that runs the test created by the test directive (see TestDirective).
    """

    name = "testcode"

    def write(
        self, build_docnames: Iterable[str], updated_docnames: Sequence[str], method: str = "update"
    ):
        assert self.env is not None
        if build_docnames is None:
            build_docnames = self.env.all_docs
        build_docnames = sorted(build_docnames)

        codes: Dict[str, str] = {}

        # Collect the code segments.
        for docname in build_docnames:
            doctree = self.env.get_doctree(docname)

            def is_code(node: nodes.Node):
                return isinstance(node, nodes.literal_block) and "testing_tested_code_name" in node

            for node in doctree.traverse(is_code):
                self.handle_code_node(node, docname, codes)

        codes_json_file = os.environ.get("DOCS_CODES_JSON_FILE")
        if codes_json_file is not None:
            with open(codes_json_file, "w") as f:
                json.dump(codes, f, indent=4)
                f.write("\n")

        if os.environ.get("DOCS_SKIP_TESTS") == "1":
            print("Skipping tests.")
        else:
            # Run the tests.
            for docname in build_docnames:
                doctree = self.env.get_doctree(docname)

                def is_test(node: nodes.Node):
                    return isinstance(node, nodes.comment) and "testing_test" in node

                for node in doctree.traverse(is_test):
                    self.handle_test_node(node, docname, codes)

    def handle_code_node(self, node, docname, codes):
        """
        Handles a tested-code node: Adds the content of the node to codes and verifies that the
        code is well-formatted.
        """
        code = node.children[0].astext()
        code_name = node["testing_tested_code_name"]
        assert (
            code_name not in codes
        ), f"Tested code segment '{code_name}' was defined more than once."
        codes[code_name] = code

        # Check formatting.
        if node["language"] == "cairo":
            # Replace patterns of the form '<expr*>' with 0 before auto-formatting.
            code_for_formatting = re.sub("<expr.*?>", "0", code)
            try:
                with set_max_line_length(MAX_LINE_LENGTH):
                    formatted_code = parse_file(code_for_formatting, filename=f"<input>").format()
            except Exception:
                traceback_str = traceback.format_exc()
                exc_str = f'Formatting failure at "{docname}:{node.line}":\n\n' + traceback_str
                print(exc_str, file=sys.stderr)
                sys.exit(1)
            if code_for_formatting.strip() != formatted_code.strip():
                print(f'Bad format at "{docname}:{node.line}". Expected:', file=sys.stderr)
                print(formatted_code, file=sys.stderr)
                print(file=sys.stderr)

                code_for_formatting_lines = code_for_formatting.strip().splitlines()
                formatted_code_lines = formatted_code.strip().splitlines()
                bad, good = [
                    (bad, good)
                    for bad, good in zip(code_for_formatting_lines, formatted_code_lines)
                    if bad != good
                ][0]
                print(f"First different line:", file=sys.stderr)
                print(bad, file=sys.stderr)
                print(good, file=sys.stderr)

                sys.exit(1)

    def handle_test_node(self, node, docname, codes):
        test_filter = os.environ.get(DOCS_TEST_FILTER_ENV_VAR)
        if test_filter is not None and re.search(test_filter, docname) is None:
            return
        try:
            if test_filter is not None:
                print(f"Running test {docname}...")
            exec(node.children[0].astext(), {"codes": codes})
        except Exception:
            traceback_str = traceback.format_exc()
            exc_str = f'Test failure at "{docname}:{node.line}":\n\n{traceback_str}'
            print(exc_str, file=sys.stderr)
            sys.exit(1)

    def get_outdated_docs(self) -> Union[str, Iterable[str]]:
        assert self.env is not None
        # Build all docs every time.
        return self.env.found_docs


def setup(app):
    app.add_directive("tested-code", TestedCodeDirective)
    app.add_directive("test", TestDirective)
    app.add_builder(TestCodeBuilder)

    return {"version": "0.1"}
