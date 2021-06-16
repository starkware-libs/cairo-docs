Common Library
==============

This page summarizes library functions available in the Cairo common library.
The common library is written in Cairo the code can be found
`here
<https://github.com/starkware-libs/cairo-lang/tree/master/src/starkware/cairo/common>`_. It
provides a level of abstraction for common and useful components that can be imported
for use in any Cairo program.

The libraries available are listed below, organized alphabetically. The functions
within each library are outlined under the relevant library heading.

-   :ref:`common_library_alloc`.

..  TODO (perama, 16/06/2021): Move the link above when the section is complete.
    -   :ref:`common_library_cairo_builtins`
    -   :ref:`common_library_default_dict`
    -   :ref:`common_library_dict`
    -   :ref:`common_library_dict_access`
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

**A note about implicit arguments**: Some descriptions state that the library function
"requires the implicit argument ``<argument>``". Where this is the case, the decision to
pass the argument follows the rule: If the parent function already has the
required argument as an implicit argument, the braces can be omitted. Otherwise, it
should be given explicitly. For example, implicit
arguments may be ``range_check_ptr`` or ``dict_ptr``. See :ref:`implicit_arguments`
for more information.

.. tested-code:: cairo library_implicits0

    # An implicit argument, x, can be passed to the parent function.
    # E.g., func function_with_implicit{x}():
    func function_with_implicit():
        # Implicit argument x is not required again.
        # E.g., library_function()
        return ()
    end

    # No implicit arguments are passed to the parent function.
    func function_without_implicit():
        # Implicit argument x is required.
        # E.g., library_function{x}()
        return ()
    end

.. _common_library_alloc:

``alloc``
---------

This section contains components from `alloc`_ in the common library.

.. _alloc: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/alloc.cairo

``alloc()``
***********

Returns a newly allocated memory segment. This is useful when defining dynamically allocated
arrays. As more elements are added, more memory will be allocated.

.. tested-code:: cairo alloc_alloc

    from starkware.cairo.common.alloc import alloc

    # Allocate a memory segment.
    let (new_slot : felt*) = alloc()

    # Allocate a memory segment for an array of structs.
    let (local my_array : MyStruct*) = alloc()

.. .. _common_library_cairo_builtins:

..  ``cairo_builtins``
..  ------------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `cairo_builtins`_ in the common library.

.. .. _cairo_builtins: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_builtins.cairo

.. .. _common_library_default_dict:

..  ``default_dict``
..  ----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `default_dict`_ in the common library.

.. .. _default_dict: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/default_dict.cairo

.. .. _common_library_dict:

..  ``dict``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `dict`_ in the common library.

.. .. _dict: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict.cairo

.. .. _common_library_dict_access:

..  ``dict_access``
..  ---------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `dict_access`_ in the common library.

.. .. _dict_access: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict_access.cairo

.. .. _common_library_find_element:

..  ``find_element``
..  ----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `find_element`_ in the common library.

.. .. _find_element: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/find_element.cairo

.. .. _common_library_hash:

..  ``hash``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `hash`_ in the common library.

.. .. _hash: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash.cairo

.. .. _common_library_hash_chain:

..  ``hash_chain``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `hash_chain`_ in the common library.

.. .. _hash_chain: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash_chain.cairo

.. .. _common_library_hash_state:

..  ``hash_state``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `hash_state`_ in the common library.

.. .. _hash_state: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash_state.cairo

.. .. _common_library_invoke:

..  ``invoke``
..  ----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `invoke`_ in the common library.

.. .. _invoke: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/invoke.cairo

.. .. _common_library_math:

..  ``math``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `math`_ in the common library.

.. .. _math: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo

.. .. _common_library_memcpy:

..  ``memcpy``
..  ----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `memcpy`_ in the common library.

.. .. _memcpy: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/memcpy.cairo

.. .. _common_library_merkle_multi_update:

..  ``merkle_multi_update``
..  -----------------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `merkle_multi_update`_ in the common library.

.. .. _merkle_multi_update: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/merkle_multi_update.cairo

.. .. _common_library_merkle_update:

..  ``merkle_update``
..  -----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `merkle_update`_ in the common library.

.. .. _merkle_update: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/merkle_update.cairo

.. .. _common_library_registers:

..  ``registers``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `registers`_ in the common library.

.. .. _registers: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/registers.cairo

.. .. _common_library_serialize:

..  ``serialize``
..  -------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `serialize`_ in the common library.

.. .. _serialize: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/serialize.cairo

.. .. _common_library_set:

..  ``set``
..  -------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `set`_ in the common library.

.. .. _set: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/set.cairo

.. .. _common_library_signature:

..  ``signature``
..  -------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `signature`_ in the common library.

.. .. _signature: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/signature.cairo

.. .. _common_library_small_merkle_tree:

..  ``small_merkle_tree``
..  ---------------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `small_merkle_tree`_ in the common library.

.. .. _small_merkle_tree: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/small_merkle_tree.cairo

.. .. _common_library_squash_dict:

..  ``squash_dict``
..  ---------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `squash_dict`_ in the common library.

.. .. _squash_dict: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/squash_dict.cairo

.. .. _common_library_uint256:

..  ``uint256``
..  -----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section contains components from `uint256`_ in the common library.

.. .. _uint256: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/uint256.cairo
