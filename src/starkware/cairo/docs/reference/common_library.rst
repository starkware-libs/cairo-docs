
``default_dict``
----------------

This section contains functions from the ``default_dict`` library.
As Cairo programs have immutable memory, dictionaries are implemented in a special way,
where dictionary updates involve the creation of intermediate dictionary states.
More information on how this works can be found in :ref:`dicts_in_cairo`.

``default_dict_new()``
**********************

Returns a new dictionary, with a default value. Must be followed by a call to
``default_dict_finalize()``.

The function requires one explicit argument:

-   ``default_value``, TODO

The function returns:

-   ``res``, a pointer to a ``DictAccess`` struct

.. tested-code:: cairo library_default_dict_new

    from starkware.cairo.common.default_dict import default_dict_new

    let new_dictionary = default_dict_new(value: felt)

``default_dict_finalize()`` function
************************************

Returns the squashed version of a ``default_dict_new`` dictionary.

.. tested-code:: cairo library_default_dict_finalize

    from starkware.cairo.common.default_dict import default_dict_finalize

    let finalized_dictionary = default_dict_finalize(new_dictionary)
