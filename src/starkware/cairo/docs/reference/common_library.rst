Common Library
==============

This page summarizes library functions available within Cairo.

The library functions are arranged alphabetically and cover the following topics:

- dictionary
    - :ref:`common_library_dict_access`
    - :ref:`common_library_dict`
    - :ref:`common_library_default_dict`
    - :ref:`common_library_squash_dict`
- array
    - :ref:`common_library_find_element`
- math
    - :ref:`common_library_math`
- hash
    - :ref:`common_library_hash`
    - :ref:`common_library_hash_chain`
    - :ref:`common_library_hash_state`
    - :ref:`common_library_small_merkle_tree`
    - :ref:`common_library_merkle_update`
    - :ref:`common_library_merkle_multi_update`
- signature
    - :ref:`common_library_signature`
- memory and state
    - :ref:`common_library_alloc`
    - :ref:`common_library_registers`
    - :ref:`common_library_cairo_builtins`
    - :ref:`common_library_memcpy`
    - :ref:`common_library_serialize`

Where a library function requires an implicit argument, passing the argument is only required if the
function lacks that argument. Example implicit arguments might be ``range_check_ptr`` or
``dict_ptr``.

.. tested-code:: cairo library_implicits0

    # Implicit argument part of function
    function{implicit_argument}():
        # Implicit argument not required again
        library_function()

.. tested-code:: cairo library_implicits1

    # Implicit argument not part of function
    function():
        # Implicit argument required
        library_function{implicit_argument}()
