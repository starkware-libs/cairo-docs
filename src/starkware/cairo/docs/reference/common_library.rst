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
-   :ref:`common_library_dict`.
-   :ref:`common_library_dict_access`.

..  TODO (perama, 16/06/2021): Move the link above when the section is complete.
    -   :ref:`common_library_cairo_builtins`
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

.. _common_library_dict:

``dict``
--------

This section refers to the common library's
`common_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict.cairo>`_
module.



``dict_update()``
*****************

Updates the value of a particular key in a dictionary. Must be passed an
implicit argument, ``dict_ptr``, of type ``DictAccess*``, representing a pointer
to the end of the dictionary. Only available for dictionaries created via ``dict_new()``
or ``default_dict_new()``.
No arguments are returned.

The function accepts the explicit arguments of type ``felt``:

-   ``key``, the key to update.
-   ``prev_value``, the current value assigned to ``key``.
-   ``new_value``, the value to be assigned to ``key``.

It is possible to get ``prev_value`` from ``__dict_manager`` using the hint:

``%{ ids.new_value = __dict_manager.get_dict(ids.dict_ptr)[ids.key] %}``

The example shows how, for a dictionary whose end pointer is ``dict_end``,
the value of a specified key can be updated.

.. tested-code:: cairo library_dict_update0

    %builtins range_check

    from starkware.cairo.common.dict import (
        dict_new, dict_write, dict_update, dict_squash)

    func main{range_check_ptr}() -> ():
        %{ initial_dict = {0: 0} %}
        let (dict_start) = dict_new()
        let dict_end = dict_start
        dict_write{dict_ptr=dict_end}(key=0, new_value=1)
        dict_update{dict_ptr=dict_end}(
            key=0, prev_value=1, new_value=2)
        return ()
    end

One can think of ``dict_update()`` as a conditional write. Passing ``prev_value``
ensures that an override will only happen in case the current value equals ``prev_value``.
Note that this is only verified at the hint level and consistency relies on eventual
squashing. Additionally, one can verify that ``dictionary[key]=value`` by calling
``dict_update(key, value, value)``.

``dict_squash()``
*****************

Squashes a dictionary represented by an array of read/write logs.
A squashed dictionary is one whose intermediate updates have been summarized and each key
appears exactly once with its most recent value. This is the only function that
asserts the consistency of the ``DictAccess`` array representing the dictionary,
a program with inconsistent dict operations can run successfully unless
we call squash (see example below).

The function uses the ``range_check`` builtin and thus
requires ``range_check_pointer`` as an implicit argument

The function accepts the explicit arguments of type ``DictAccess*``:

-   ``dict_accesses_start``, a pointer to the start of the dictionary (first operation).
-   ``dict_accesses_end``, a pointer to the end of the dictionary (last operation).

The function returns two arguments of type ``DictAccess*``:

-   ``squashed_dict_start``, a pointer to the start of the squashed dictionary.
-   ``squashed_dict_end``, a pointer to the end of the squashed dictionary.

The only operation that uses ``dict_accesses_start`` is the ``dict_squash()`` function. All
other dictionary operations append to the array of ``DictAccess`` instances.

.. tested-code:: cairo library_dict_squash

    %builtins range_check

    from starkware.cairo.common.dict import (
        dict_new, dict_write, dict_update, dict_squash)

    func main{range_check_ptr}() -> ():
        %{ initial_dict = {0: 0} %}
        let (dict_start) = dict_new()
        let dict_end = dict_start
        dict_write{dict_ptr=dict_end}(0, 1)
        dict_update{dict_ptr=dict_end}(0, 1, 2)
        let (squashed_dict_start, squashed_dict_end) = dict_squash{
            range_check_ptr=range_check_ptr}(dict_start, dict_end)
        # The following is an inconsistent update, 'prev_value'
        # is now '2'. This will fail while using the library's hints
        # but can be made to pass by a malicious prover.
        dict_update{dict_ptr=squashed_dict_end}(
            key=0, prev_value=3, new_value=2)
        # Squash fails.
        let (squashed_dict_start, squashed_dict_end) = dict_squash{
            range_check_ptr=range_check_ptr}(
            squashed_dict_start, squashed_dict_end)
        return ()
    end

.. _common_library_dict_access:

``dict_access``
---------------

This section refers to the common library's
`common_dict_access <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict_access.cairo>`_
module.

``DictAccess``
**************

A struct specifying the ``DictAccess`` memory structure. Cairo simulates dictionaries
by an array of read-modify-write instructions, which are specified by the ``DictAccess`` struct.
The consistency of such an array can be verified by applying ``squash_dict()``.

For libraries that abstract away Cairo's representation of dictionaries and allow a more
standard dictionary interface than what will be shown here, see the
``dict`` and ``default_dict`` modules in the common library.

The struct has the following members of type ``felt``:

-   ``key``, the key of a key-value pair.
-   ``prev_value``, the previous value iof a key-value pair.
-   ``new_value``, the current value of a key-value pair.

In the example below, a dictionary is created by adding ``DictAccess`` structs to an array
and manually incrementing a pointer to the end of the array.

.. tested-code:: cairo library_dictaccess0

    %builtins range_check

    from starkware.cairo.common.dict import dict_squash
    from starkware.cairo.common.squash_dict import squash_dict
    from starkware.cairo.common.alloc import alloc
    from starkware.cairo.common.dict_access import DictAccess

    func main{range_check_ptr}() -> ():
        alloc_locals
        let (dict_start : DictAccess*) = alloc()
        assert [dict_start] = DictAccess(
            key=0, prev_value=100, new_value=100)
        assert [dict_start + DictAccess.SIZE] = DictAccess(
            key=1, prev_value=200, new_value=200)

        let dict_end = dict_start + 2 * DictAccess.SIZE
        # (dict_start, dict_end) now represent the dictionary
        # {0: 100, 1: 200}.

        # Now pass the dictionary to a function for inspection.
        check_key_ratio{dict_ptr=dict_end}(a=0, b=1)

        # Squash the dictionary from an array of 4 DictAccess structs
        # to an array of 2, with a single DictAccess entry per key.
        # Fails if the prover changed 'value_a' and 'value_b'.
        let (local squashed_dict_start : DictAccess*) = alloc()
        let (squashed_dict_end) = squash_dict{
            range_check_ptr=range_check_ptr}(
            dict_start, dict_end, squashed_dict_start)
        return ()
    end

``check_key_ratio()`` checks that the value at key ``b`` is double the value at key ``a``.
This will only be enforced if we eventually call ``squash_dict()``.

.. tested-code:: cairo library_dictaccess1

    func check_key_ratio{dict_ptr : DictAccess*}(a : felt, b : felt):
        alloc_locals
        # Adds more DictAccess entries to the existing array.
        # Values match previous entries and will be squashed.
        local value_a
        local value_b
        %{
            ids.value_a = 100  # Malicious prover may change.
            ids.value_b = 200
        %}
        assert value_a * 2 = value_b
        # Simulate dictionary read by appending a 'DictAccess'
        # instruction with 'prev_value=new_value=current_value'.
        assert [dict_ptr] = DictAccess(
            key=a, prev_value=value_a, new_value=value_a)
        assert [dict_ptr + DictAccess.SIZE] = DictAccess(
            key=b, prev_value=value_b, new_value=value_b)
        let dict_end = dict_ptr + 2 * DictAccess.SIZE
        # A call to squash_dict() will ensure that the prover
        # used values that are consistent with the input dictionary.
        return ()
    end

.. .. _common_library_find_element:

..  ``find_element``
..  ----------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_find_element <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/find_element.cairo>`_
    module.

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
