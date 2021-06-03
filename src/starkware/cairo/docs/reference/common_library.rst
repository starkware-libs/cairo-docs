Common Library
==============

This page summarizes library functions available in the Cairo common library.
The common library is written in Cairo can be found here
`Cairo common library
<https://github.com/starkware-libs/cairo-lang/tree/master/src/starkware/cairo/common>`_. It
providesa a level of abstraction for common and useful components that can be imported
for use in any Cairo program.

The libraries available are listed below, organized alphabetically. The functions
within each library are outlined under the relevant library heading.

-   :ref:`common_library_alloc`.
-   :ref:`common_library_cairo_builtins`
-   :ref:`common_library_dict`
-   :ref:`common_library_dict_access`
-   :ref:`common_library_default_dict`
-   :ref:`common_library_find_element`
-   :ref:`common_library_hash`
-   :ref:`common_library_hash_chain`
-   :ref:`common_library_hash_state`
-   :ref:`common_library_invoke`
-   :ref:`common_library_math`
-   :ref:`common_library_memcpy`
-   :ref:`common_library_merkle_multi_update`
-   :ref:`common_library_merkle_update`
-   :ref:`common_library_registers`
-   :ref:`common_library_serialize`
-   :ref:`common_library_set`
-   :ref:`common_library_signature`
-   :ref:`common_library_small_merkle_tree`
-   :ref:`common_library_squash_dict`
-   :ref:`common_library_uint256`

Where a library function requires an implicit argument, passing the argument is only required if the
function lacks that argument. Example implicit arguments might be ``range_check_ptr`` or
``dict_ptr``. See :ref:`implicit_arguments` for more information.

.. tested-code:: cairo library_implicits0

    func function_with_implicit{range_check_ptr}():
        # Implicit argument is not required again
        library_function()
        return ()
    end

    func function_without_implicit():
        # Implicit argument is required
        library_function{range_check_ptr}()
        return ()
    end

``alloc`` library
-----------------

``alloc()`` function
********************

Returns a newly allocated memory segment. This is useful when defining dynamically allocated
arrays. As more elements are added, more memory can be allocated.

.. tested-code:: cairo alloc_alloc

    from starkware.cairo.common.alloc import alloc

    # Allocate a memory segment.
    let new_slot = alloc()

    # Allocate a memory segment for an array of structs.
    let (local my_array : MyStruct) = alloc()
