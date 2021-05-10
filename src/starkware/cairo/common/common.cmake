python_lib(cairo_common_lib
    PREFIX starkware/cairo/common
    FILES
    alloc.cairo
    cairo_builtins.cairo
    default_dict.cairo
    dict.cairo
    dict_access.cairo
    dict.py
    find_element.cairo
    hash_chain.cairo
    hash_chain.py
    hash_state.cairo
    hash.cairo
    math_utils.py
    math.cairo
    memcpy.cairo
    merkle_multi_update.cairo
    merkle_update.cairo
    registers.cairo
    serialize.cairo
    signature.cairo
    small_merkle_tree.cairo
    small_merkle_tree.py
    squash_dict.cairo
    ${CAIRO_COMMON_LIB_ADDITIONAL_FILES}

    LIBS
    cairo_vm_crypto_lib
    starkware_merkle_tree_lib
    ${CAIRO_COMMON_LIB_ADDITIONAL_LIBS}
)

python_lib(cairo_common_test_utils_lib
    PREFIX starkware/cairo/common

    FILES
    ${CAIRO_COMMON_TEST_UTILS_LIBS_ADDITONAL_FILES}

    LIBS
    cairo_common_lib
    cairo_compile_lib
    cairo_run_builtins_lib
    cairo_run_lib
    cairo_tracer_lib
    cairo_vm_lib
)
