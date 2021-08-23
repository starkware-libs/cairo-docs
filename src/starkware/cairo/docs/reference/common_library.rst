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
to the end of the dictionary. Only available for dictionaries created via ``dict_new()``.
No arguments are returned.

The function accepts the explicit arguments of type ``felt``:

-   ``key``, the key to update of a key-value pair.
-   ``prev_value``, the current value assigned to ``key``.
-   ``new_value``, the value to be assigned to ``key``.

It is possible to get ``prev_value`` from ``__dict_manager`` using the hint:
```
%{ ids.new_value = __dict_manager.get_dict(ids.dict_ptr)[ids.key] %}
```

The example shows how, for a dictionary whose pointer is ``my_dict``,
the value of a specified key can be updated.

.. tested-code:: cairo library_dict_update

    from starkware.cairo.common.dict import dict_update
    from starkware.cairo.common.dict_access import DictAccess

    # my_dict has key:val pairs {5: 8, 12: 35, 33: 198}.

    # The value associated with key=12 is changed.
    dict_update{dict_ptr=my_dict}(12, 35, 34)

    # my_dict has key:val pairs {1: 2, 5: 8, 12: 34, 33: 198}.
    let (value) = dict_read{dict_ptr=my_dict}(12)
    assert value = 34

Unlike ``dict_write()``, this function does not allow new keys to be added to the
dictionary (recall that this is only enforced at the hint level, a malicious
prover can use dict_update to add new keys).

``dict_squash()``
*****************

Squashes a dictionary represented by an array of read/write logs.
A squashed dictionary is one whose intermediate updates have been summarized and each key
appears exactly once with its most recent value. This is the only function that
asserts the consistency of the DictAccess array representing the dictionary,
a program with inconsistent dict operations can run successfully unless
we call squash (see example below).

The function uses the ``range_check`` builtin and thus
requires ``range_check_pointer`` as an implicit argument

The function accepts the explicit arguments of type ``DictAccess*``:

-   ``dict_accesses_start``, a pointer to the initial dictionary state.
-   ``dict_accesses_end``, a pointer to the latest dictionary state.

The function returns two arguments of type ``DictAccess*``:

-   ``squashed_dict_start``, a pointer to the initial dictionary state.
-   ``squashed_dict_end``, a pointer to the latest dictionary state.

In order for the initial state to be available to pass to the function,
it is convention to save the state before updates are applied.
In the example below, ``my_dict_saved`` is a reference to the the dictionary state
that was made prior to updates being applied.

.. tested-code:: cairo library_dict_squash

    from starkware.cairo.common.dict import dict_squash

    let (squashed_dict_start, squashed_dict_end) = dict_squash(
        dict_accesses_start=my_dict_saved,
        dict_accesses_end=my_dict)

.. _common_library_dict_access:

``dict_access``
---------------

This section refers to the common library's
`common_dict_access <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/dict_access.cairo>`_
module.

``DictAccess``
**************

A struct specifying the ``DictAccess`` memory structure.
This struct is used by functions from the common library that use dictionaries.
For example, the ``dict_read()`` function accepts an implicit argument ``dict_ptr``
of type ``DictAccess*``, which is used to locate the dictionary in memory.

A modified dictionary is composed of a sequence of "intermediate" ``DictAccess`` instances.
Each instance consists of a key, the previous value and the new value assigned during
a particular modification.

The struct has the following members of type ``felt``:

-   ``key``, the key of a key-value pair.
-   ``prev_value``, the previous value of a key-value pair.
-   ``new_value``, the current value of a key-value pair.

In the example below, a dictionary called ``dict_start`` is initialized with an expandable
memory to accomodate modifications. Each new modification would append a new ``DictAccess``
instance to that section of memory. ``dict_start`` is a local variable assigned to
a pointer to the beginning of the first ``DictAccess`` instance of that dictionary.

.. tested-code:: cairo library_dictaccess

    from starkware.cairo.common.dict_access import DictAccess
    from starkware.cairo.common.alloc import alloc

    let (local dict_start : DictAccess*) = alloc()

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
