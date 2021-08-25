file(GLOB_RECURSE RST_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.rst)
file(GLOB_RECURSE TEMPLATE_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} _templates/*.html)

python_lib(cairo_docs_lib
    PREFIX starkware/cairo/docs

    FILES
    test_utils.py

    LIBS
    cairo_compile_lib
    pip_isort
)

python_venv(cairo_docs_venv
    PYTHON python3.7

    LIBS
    cairo_common_lib
    cairo_docs_lib
    cairo_function_runner_lib
    cairo_run_lib
    cairo_script_lib
    cairo_syntax_highlighting_lib
    starknet_compile_test_utils_lib
    pip_pytest
    pip_sphinx
)

get_target_property(VENV_PYTHON cairo_docs_venv VENV_PYTHON)
get_target_property(VENV_STAMP cairo_docs_venv STAMP_FILE)

add_custom_command(
    OUTPUT "external/html/index.html"
    COMMAND ${VENV_PYTHON}
        -m sphinx.cmd.build
        -M html "${CMAKE_CURRENT_SOURCE_DIR}" "${CMAKE_CURRENT_BINARY_DIR}/external" -W
    COMMENT "Generating Cairo docs..."
    DEPENDS cairo_docs_venv ${VENV_STAMP} ${RST_FILES} ${TEMPLATE_FILES}
)

add_custom_command(
    OUTPUT "internal/html/index.html"
    COMMAND ${VENV_PYTHON}
        -m sphinx.cmd.build
        -M html "${CMAKE_CURRENT_SOURCE_DIR}" "${CMAKE_CURRENT_BINARY_DIR}/internal" -W
        -t internal
    COMMENT "Generating Cairo docs..."
    DEPENDS cairo_docs_venv ${VENV_STAMP} ${RST_FILES} ${TEMPLATE_FILES}
)

add_custom_target(cairo_docs_html ALL
    DEPENDS "external/html/index.html" "internal/html/index.html"
)

python_exe(cairo_docs_test
    VENV cairo_docs_venv
    MODULE sphinx.cmd.build
    ARGS "-M testcode ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}"
    ENVIRONMENT_VARS "DOCS_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}"
)

add_test(
    NAME cairo_docs_test
    COMMAND ${CMAKE_CURRENT_BINARY_DIR}/cairo_docs_test
)

set (CODES_JSON_PATH "${CMAKE_CURRENT_BINARY_DIR}/codes.json")
add_custom_command(
    OUTPUT ${CODES_JSON_PATH}
    COMMAND DOCS_SKIP_TESTS=1 DOCS_CODES_JSON_FILE=${CODES_JSON_PATH}
        ${CMAKE_CURRENT_BINARY_DIR}/cairo_docs_test
    DEPENDS cairo_docs_test ${RST_FILES} testing.py
)

python_lib(cairo_codes_json_lib
    PREFIX starkware/cairo/docs

    ARTIFACTS
    "${CODES_JSON_PATH} codes.json"
)

full_python_test(cairo_docs_additional_tests
    PREFIX starkware/cairo/docs
    PYTHON python3.7
    TESTED_MODULES starkware/cairo/docs

    FILES
    hello_cairo/sum_by_key_solution_test.py
    hello_cairo/sum_by_key_solution.cairo

    LIBS
    cairo_common_lib
    cairo_compile_lib
    cairo_function_runner_lib
    pip_pytest
)
