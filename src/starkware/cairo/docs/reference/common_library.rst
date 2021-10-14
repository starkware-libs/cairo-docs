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
-   :ref:`common_library_bitwise`.
-   :ref:`common_library_default_dict`.
-   :ref:`common_library_find_element`.

..  TODO (perama, 16/06/2021): Move the link above when the section is complete.
    -   :ref:`common_library_cairo_builtins`
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

.. _common_library_bitwise:

``bitwise``
-----------

This section refers to the common library's
`common_bitwise <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/bitwise.cairo>`_
module.

``bitwise_and()``
*****************

Returns the result of the bitwise AND operation of two elements. Requires an implicit
argument, ``bitwise_ptr`` of type ``BitwiseBuiltin*``.

The function accepts the explicit arguments:

-   ``x`` of type ``felt``, the first operand.
-   ``y`` of type ``felt``, the second operand.

The function returns the value:

-   ``x_and_y`` of type ``felt``, the result of the bitwise ``AND`` operation ``a & b``.

The example below shows the operation on binary inputs ``1100`` and ``1010``
results in ``1000``:

.. tested-code:: cairo library_bitwise_and

    from starkware.cairo.common.bitwise import bitwise_and

    let (result) = bitwise_and(12, 10)  # Binary (1100, 1010).
    assert result = 8  # Binary 1000.

``bitwise_xor()``
*****************

Returns the result of the bitwise XOR operation on two elements. Requires an implicit
argument, ``bitwise_ptr`` of type ``BitwiseBuiltin*``.

The function accepts the explicit arguments:

-   ``x`` of type ``felt``, the first operand.
-   ``y`` of type ``felt``, the second operand.

The function returns the value:

-   ``x_xor_y`` of type ``felt``, the result of the bitwise ``XOR`` operation ``a ^ b``.

The example below shows the operation on binary inputs ``1100`` and ``1010``
results in ``0110``:

.. tested-code:: cairo library_bitwise_xor

    from starkware.cairo.common.bitwise import bitwise_xor

    let (result) = bitwise_xor(12, 10)  # Binary (1100, 1010).
    assert result = 6  # Binary 0110.

``bitwise_or()``
****************

Returns the result of the bitwise OR operation on two elements. Requires an implicit
argument, ``bitwise_ptr`` of type ``BitwiseBuiltin*``.

The function accepts the explicit arguments:

-   ``x`` of type ``felt``, the first operand.
-   ``y`` of type ``felt``, the second operand.

The function returns the value:

-   ``x_or_y`` of type ``felt``, the result of the bitwise ``OR`` operation ``a | b``.

The example below shows the operation on binary inputs ``1100`` and ``1010``
results in ``1110``:

.. tested-code:: cairo library_bitwise_or

    from starkware.cairo.common.bitwise import bitwise_or

    let (result) = bitwise_or(12, 10)  # Binary (1100, 1010).
    assert result = 14  # Binary 1110.

``bitwise_operations()``
************************

Returns the result of the bitwise AND, XOR and OR operations on two elements. Requires
an implicit argument, ``bitwise_ptr`` of type ``BitwiseBuiltin*``.

The function accepts the explicit arguments:

-   ``x`` of type ``felt``, the first operand.
-   ``y`` of type ``felt``, the second operand.

The function returns the values:

-   ``x_and_y`` of type ``felt``, the result of the bitwise ``AND`` operation ``a & b``.
-   ``x_xor_y`` of type ``felt``, the result of the bitwise ``XOR`` operation ``a ^ b``.
-   ``x_or_y`` of type ``felt``, the result of the bitwise ``OR`` operation ``a | b``.

The example below shows the operation on binary inputs ``1100`` and ``1010``
results in ``1000``, ``0110`` and ``1110``:

.. tested-code:: cairo library_bitwise_operations

    from starkware.cairo.common.bitwise import bitwise_operations

    # Binary (1100, 1010).
    let (and, xor, or) = bitwise_operations(12, 10)
    assert and = 8  # Binary 1000.
    assert xor = 6  # Binary 0110.
    assert or = 14  # Binary 1110.

.. _common_library_default_dict:

``default_dict``
----------------

This section refers to the common library's
`default_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/default_dict.cairo>`_
module.

``default_dict_new()``
**********************

Returns a new dictionary where all keys are initialized with a given default value.
One can interact with the dictionary using the ``dict_read()``, ``dict_write()``
operations discussed in the ``dict`` module.
Note that in order to enforce the consistency of subsequent dictionary accesses with
the default values, one must eventually call ``default_dict_finalize()`` (which in turn calls
``dict_squash()``, as discussed in that section). Otherwise, this is only enforced at the
hints level which can be changed by a malicious prover.

..  TODO (perama, 29/08/21): Add links when available (dict module, DictAccess dict_squash).

The function requires the explicit argument:

-   ``default_value``, the default value.

The function returns:

-   ``res``, of type ``DictAccess*``, a pointer to the new dictionary.

``default_dict_finalize()``
***************************

Squashes the dictionary and verifies consistency with respect to the default value.
A squashed dictionary is one whose intermediate updates have been summarized and each
key appears exactly once with its most recent value.
For more details see ``dict_squash()`` from the ``dict`` module.

..  TODO (perama, 29/08/21): Add link when available (dict_squash).

The function requires the explicit arguments:

-   ``dict_accesses_start``, a pointer to the initial dictionary (first operation).
-   ``dict_accesses_end``, a pointer to the end of the dictionary (last operation).
-   ``default_value``, the expected initial value of each key.

The function returns the values:

-   ``squashed_dict_start``, a pointer to the start of the squashed dictionary.
-   ``squashed_dict_end``, a pointer to the end of the squashed dictionary.

Note that one must eventually call ``default_dict_finalize()`` to verify both the internal
consistency of the ``DictAccess`` entries forming the dictionary and of the consistency
with the default value.

In the example below we create and finalize a default dictionary, and explain what
may happen if ``default_dict_finalize()`` is not called.

Example
*******

.. tested-code:: cairo library_default_dict_finalize

    %builtins range_check

    from starkware.cairo.common.default_dict import (
        default_dict_new, default_dict_finalize)
    from starkware.cairo.common.dict import dict_write, dict_update

    func main{range_check_ptr}() -> ():
        alloc_locals
        let (local my_dict_start) = default_dict_new(default_value=7)
        let my_dict = my_dict_start
        dict_write{dict_ptr=my_dict}(key=0, new_value=8)
        let (my_dict_start, my_dict) = default_dict_finalize(
            my_dict_start, my_dict, 7)
        # The following is an inconsistent update, the entry with
        # key 1 still contains the default value 7.
        # This will fail while using the library's hints
        # but can be made to pass by a malicious prover.

        # Update fails for an honest prover (commented out).
        # dict_update{dict_ptr=my_dict}(key=1, prev_value=8, new_value=9)

        # Finalize fails for the malicious prover with extra update.
        let (my_dict_start, my_dict) = default_dict_finalize(
            my_dict_start, my_dict, 7)
        return ()
    end

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
