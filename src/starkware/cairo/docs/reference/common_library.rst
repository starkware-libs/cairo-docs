
``default_dict``
----------------

This section contains functions from the ``default_dict`` library.
As Cairo programs have immutable memory, dictionaries are implemented in a special way,
where dictionary updates involve the creation of intermediate dictionary states.
More information on how this works can be found in :ref:`dicts_in_cairo`.

``default_dict_new()``
**********************

Returns a new dictionary, with a default value. Must be followed by a call to
``default_dict_finalize()``. Default dictionaries are useful where access to
create dictionaries where a certain key does not yet exist. Rather than raise
and exception, the key will be set to ``default_value``.

The function requires one explicit argument:

-   ``default_value``, a ``felt`` that will be set as the value if
    the key does not yet exist.

The function returns:

-   ``res``, a pointer to a ``DictAccess`` struct.

In the code below, an empty default dictionary is made and finalized. Then a key which
does not exist is updated. This triggers the value to be set to the default value for
that new key.

.. tested-code:: cairo library_default_dict_new

    from starkware.cairo.common.default_dict import default_dict_new
    from starkware.cairo.common.default_dict import default_dict_finalize
    from starkware.cairo.common.dict import dict_write

    # Create a new default dict with no starting values.
    let (local new_dictionary) = default_dict_new(7)
    # Finalize dict.
    let local (_, new_dictionary) = default_dict_finalize(
        new_dictionary, new_dictionary, 7)

    # Update dict. Key 35 does not exist, default will be used.
    # Adds the key=35, val=7 to the dict. 3 is not used.
    dict_update(new_dictionary, 35, 0, 3)
    # Finalize dictionary again.
    let local (_, new_dictionary)  = default_dict_finalize(
        new_dictionary, new_dictionary, 7)

``default_dict_finalize()`` function
************************************

Returns the squashed version of a ``default_dict_new`` dictionary. The function is
used to remove the intermediate dictionary states. That is, if a dictionary has
been populated with new elements and had values changed, this function

The function requires three explicit arguments:

-   ``dict_accesses_start``, a pointer ``DictAccess*``, to the initial value of the dictionary.
-   ``dict_accesses_end``, a pointer ``DictAccess*``, to the latest value of the dictionary.
-   ``default_value``, the default value specified whe this dictionary was created.

The function returns:

-   ``squashed_dict_start``, a pointer to the initial state of the dictionary.
-   ``squashed_dict_end``, a pointer to the final state of the dictionary.

.. tested-code:: cairo library_default_dict_finalize

    from starkware.cairo.common.default_dict import default_dict_finalize

    let (local original, updated) = default_dict_finalize(new_dictionary)
