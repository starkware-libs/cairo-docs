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

-   :ref:`common_library_alloc`
-   :ref:`common_library_find_element`

..  TODO (perama, 16/06/2021): Move the link above when the section is complete.
    -   :ref:`common_library_cairo_builtins`
    -   :ref:`common_library_default_dict`
    -   :ref:`common_library_dict`
    -   :ref:`common_library_dict_access`
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

In the example below, two of the three functions require the implicit argument ``x``.
In ``function_without_implicit_arg()``, a function is called passing argument ``x`` explicitly.
In ``function_with_implicit_arg{x}()``, a function is called passing argument ``x`` implicitly.

.. tested-code:: cairo library_implicits0

    func function_without_implicit_arg():
        let x = 0
        # x must be passed explicitly since it's not an
        # implicit argument of this function.
        function_with_implicit_arg{x=x}()
        return ()
    end

    func function_with_implicit_arg{x}():
        # x is an implicit argument of this function
        # so it does not need to be passed explicitly.
        another_function_with_implicit_arg()
        return ()
    end

    func another_function_with_implicit_arg{x}():
        return ()
    end

.. _common_library_alloc:

``alloc``
---------

This section refers to the common library's
`alloc <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/alloc.cairo>`_
module.

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
    This section refers to the common library's
    `common_cairo_builtins <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_builtins.cairo>`_
    module.

.. .. _common_library_default_dict:

..  ``default_dict``
..  ----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_default_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/default_dict.cairo>`_
    module.

.. .. _common_library_dict:

..  ``dict``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict.cairo>`_
    module.

.. .. _common_library_dict_access:

..  ``dict_access``
..  ---------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_dict_access <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict_access.cairo>`_
    module.

.. _common_library_find_element:

``find_element``
----------------

This section refers to the common library's
`find_element <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/find_element.cairo>`_
module.

``find_element()``
******************

Returns the pointer to an element in an array whose key matches a specified key. The function
requires the implicit argument ``range_check_ptr``. Note that if the array contains
multiple elements with the requested key, the function may return a pointer to any of them.

The function requires four explicit arguments:

-   ``array_ptr``, a pointer to an array.
-   ``elm_size``, the size (in memory cells) of each element in the array.
-   ``n_elms``, the number of elements in the array.
-   ``key``, the key to look for (the key is assumed to be the first member of
    each element in the array).

The function returns:

-   ``elm_ptr``, the pointer to an element whose first memory cell is ``key``
    (namely, ``[elm_ptr]=key``).

The function has the ability to receive the index of that element via a hint, which may
save proving time. If ``key`` is not found then a ``ValueError`` exception
will be raised while processing the library's hint. Note that a malicious prover
can't cause ``find_element()`` to succeed by changing the hint, as the Cairo
program will fail when the key is not present in the array.

.. tested-code:: cairo library_find_element

    %builtins range_check
    from starkware.cairo.common.find_element import find_element
    from starkware.cairo.common.alloc import alloc

    struct MyStruct:
        member a : felt
        member b : felt
    end

    func main{range_check_ptr}() -> ():
        # Create an array with MyStruct elements (1,2), (3,4), (5,6).
        alloc_locals
        let (local array_ptr : MyStruct*) = alloc()
        assert array_ptr[0] = MyStruct(a=1, b=2)
        assert array_ptr[1] = MyStruct(a=3, b=4)
        assert array_ptr[2] = MyStruct(a=5, b=6)

        # Find any element with key '5'.
        let (element_ptr : MyStruct*) = find_element(
            array_ptr=array_ptr,
            elm_size=MyStruct.SIZE,
            n_elms=3,
            key=5)
        # A pointer to the element with index 2 is returned.
        assert element_ptr.a = 5
        assert element_ptr.b = 6

        # Pass a known index in a hint to save proving time.
        %{ __find_element_index = 2 %}
        let (element_ptr : MyStruct*) = find_element(
            array_ptr=array_ptr,
            elm_size=MyStruct.SIZE,
            n_elms=3,
            key=5)
        assert element_ptr.a = 5
        assert element_ptr.b = 6
        return ()
    end

``search_sorted_lower()``
*************************

Returns the pointer to the first element in the array whose first field is at least ``key``.
The array elements must be sorted by the first field in ascending order. If no such item exists,
it returns a pointer to the end of the array. The function requires the implicit argument
``range_check_ptr``.

The function accepts the arguments:

-  ``array_ptr``, a pointer to a sorted array.
-  ``elm_size``, the size of (in memory cells) of each element in the array.
-  ``n_elms``, the number of elements in the array.
-  ``key``, the key lower bound (the key is assumed to be the first member of
   each element in the array).

The function returns:

-  ``elm_ptr``, the pointer to the first element whose key is greater or equal to the lower bound.

Continuing with the example above, with lower bound ``2``, the middle element is returned.

.. tested-code:: cairo library_search_sorted_lower

    from starkware.cairo.common.find_element import (
        search_sorted_lower)

    let (smallest_ptr : MyStruct*) = search_sorted_lower(
        array_ptr=array_ptr, elm_size=2, n_elms=3, key=2)
    assert smallest_ptr.a = 3
    assert smallest_ptr.b = 4

``search_sorted()``
*******************

Returns both the pointer to the first element in the array whose key matches a specified key, and
an indicator for the success of the search. The array elements must be sorted by the
first field in ascending order. If no such item exists, returns an undefined pointer,
and ``success=0``. The function requires the implicit argument ``range_check_ptr``.

The function accepts the arguments:

-  ``array_ptr``, the pointer to a sorted array.
-  ``elm_size``, the size (in memory cells) of each element in the array.
-  ``n_elms``, the number of elements in the array.
-  ``key``, the key to look for (the key is assumed to be the first member of
   each element in the array).

The function returns:

-  ``elm_ptr``, the pointer to the first element whose first member is ``key``,
   namely ``[elm_ptr] = key``.
-  ``success``, a ``felt`` which equals ``1`` if the key was found and ``0`` otherwise.

Continuing with the same example, since the array is sorted, searching for the key
``5`` leads to the last element.

.. tested-code:: cairo library_search_sorted

    from starkware.cairo.common.find_element import search_sorted

    let (first_ptr : MyStruct*, success_val) = search_sorted(
        array_ptr=array_ptr, elm_size=2, n_elms=3, key=5)
    assert success_val = 1
    assert first_ptr.a = 5
    assert first_ptr.b = 6

.. .. _common_library_hash:

..  ``hash``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_hash <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash.cairo>`_
    module.

.. .. _common_library_hash_chain:

..  ``hash_chain``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_hash_chain <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash_chain.cairo>`_
    module.

.. .. _common_library_hash_state:

..  ``hash_state``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_hash_state <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/hash_state.cairo>`_
    module.

.. .. _common_library_invoke:

..  ``invoke``
..  ----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_invoke <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/invoke.cairo>`_
    module.

.. .. _common_library_math:

..  ``math``
..  --------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_math <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo>`_
    module.

.. .. _common_library_memcpy:

..  ``memcpy``
..  ----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_memcpy <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/memcpy.cairo>`_
    module.

.. .. _common_library_merkle_multi_update:

..  ``merkle_multi_update``
..  -----------------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_merkle_multi_update <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/merkle_multi_update.cairo>`_
    module.

.. .. _common_library_merkle_update:

..  ``merkle_update``
..  -----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_merkle_update <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/merkle_update.cairo>`_
    module.

.. .. _common_library_registers:

..  ``registers``
..  --------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_registers <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/registers.cairo>`_
    module.

.. .. _common_library_serialize:

..  ``serialize``
..  -------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_serialize <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/serialize.cairo>`_
    module.

.. .. _common_library_set:

..  ``set``
..  -------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_set <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/set.cairo>`_
    module.

.. .. _common_library_signature:

..  ``signature``
..  -------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_signature <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/signature.cairo>`_
    module.

.. .. _common_library_small_merkle_tree:

..  ``small_merkle_tree``
..  ---------------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_small_merkle_tree <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/small_merkle_tree.cairo>`_
    module.

.. .. _common_library_squash_dict:

..  ``squash_dict``
..  ---------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_squash_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/squash_dict.cairo>`_
    module.

.. .. _common_library_uint256:

..  ``uint256``
..  -----------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_uint256 <://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/uint256.cairo>`_
    module.
