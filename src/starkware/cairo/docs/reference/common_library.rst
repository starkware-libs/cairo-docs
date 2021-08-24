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

..  TODO (perama, 16/06/2021): Move the link above when the section is complete.
    -   :ref:`common_library_cairo_builtins`
    -   :ref:`common_library_default_dict`
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
module for working with user defined dicts, abstracting away Cairo's simulation
of dictionaries as an array of read/write logs.

``dict_new()``
**************

Returns a new dictionary. The function does not require any arguments.
A new dictionary is initially populated by using a hint with the
expression ``initial_dict``. The dictionary associated with that expression
will be found by the ``__dict_manager``.

Note that Cairo has no way to enforce that subsequent read/writes are consistent
with the ``initial_dict`` hint (this is only enforced at the python level). Technically, the
return value is a pointer to an empty ``DictAccess`` array. Soundness with respect to the
initial values can only be achieved with explicit initialization of the dictionary or
by using the ``default_dict_new()`` from the
`common_default_dict <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/default_dict.cairo>`_
module instead, which is not based on hints (and is thus also
available in StarkNet, unlike ``dict_new()``).

The function returns the argument:

-   ``res``, of type ``DictAccess*``, a pointer to the new dictionary.

.. tested-code:: cairo library_dict_new

    from starkware.cairo.common.dict import dict_new
    from starkware.cairo.common.dict_access import DictAccess

    alloc_locals
    %{
        initial_dict = {
            5: 8,
            12: 35,
            33: 198
        }
    %}
    let (local my_dict : DictAccess*) = dict_new()
    # 'my_dict' is now associated with the hint's 'initial_dict'.

``dict_read()``
***************

Returns the value of a specified dictionary key. Must be passed an implicit argument,
``dict_ptr``, of type ``DictAccess*``, representing the pointer to the end of the dictionary.
Only available for dictionaries created via ``dict_new()``.

The function accepts the explicit argument:

-   ``key``, of type ``felt``, the requested key.

The function returns the argument:

-   ``value``, of type ``felt``, the value assigned to ``key``.

The example below shows, for an existing dictionary whose end pointer is ``my_dict``,
how the value associated with the key ``12`` can be read. Note how the pointer ``my_dict``
is passed as an implicit argument.

.. tested-code:: cairo library_dict_read

    from starkware.cairo.common.dict import dict_read

    # my_dict has key:val pairs {5: 8, 12: 35, 33: 198}.
    let (local val : felt) = dict_read{dict_ptr=my_dict}(key=12)
    assert val = 35

``dict_write()``
****************

Writes a value to the dictionary, overriding the existing value. Must be passed a
pointer to the end of the dictionary, ``dict_ptr``, of type ``DictAccess*``, as an implicit
argument. No values are returned. Only available for dictionaries
created via ``dict_new()``.

The function accepts the explicit arguments:

-   ``key``, of type ``felt``, the key to write.
-   ``new_value``, of type ``felt``, the value to be assigned to ``key``.

The example below shows how, for an existing dictionary whose pointer is ``my_dict``,
the value associated with the key ``12`` can be changed from ``35`` to ``34``.
Note how the pointer ``my_dict`` is passed as an implicit argument.

.. tested-code:: cairo library_dict_write

    from starkware.cairo.common.dict import dict_write

    # my_dict has key:val pairs {5: 8, 12: 35, 33: 198}.

    # The value associated with key=12 is changed.
    dict_write{dict_ptr=my_dict}(key=12, new_value=34)
    dict_write{dict_ptr=my_dict}(key=1, new_value=2)

    let key_12_val = dict_read{dict_ptr=my_dict}(key=12)
    assert key_12_val = 34
    let key_1_val = dict_read{dict_ptr=my_dict}(key=1)
    assert key_1_val = 2

.. .. _common_library_dict_access:

..  ``dict_access``
..  ---------------

..  TODO (perama, 16/06/2021): Uncomment the link when the section is complete.
    This section refers to the common library's
    `common_dict_access <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict_access.cairo>`_
    module.

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
