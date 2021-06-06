
``dict``
--------

This section contains functions from the ``dict`` library.

``dict_new()``
**************

Returns a new dictionary.

.. tested-code:: cairo library_dict_new

    from starkware.cairo.common.dict import dict_new

    let new_dict = new_dict()

``dict_read()``
***************

Returns the value of a dictionary read. Must be passed an implicit argument pointing to the most
recent version of the dictionary.

.. tested-code:: cairo library_dict_read

    from starkware.cairo.common.dict import dict_read

    let result = dict_read{dict_ptr : DictAccess*}(dict_key)

``dict_write()``
****************

Writes a value to the dictionary, overriding the existing value. Must be passed an implicit argument
pointing to the most recent version of the dictionary. No values are returned.

.. tested-code:: cairo library_dict_write

    from starkware.cairo.common.dict import dict_write

    dict_write{dict_ptr : DictAccess*}(
        key : felt,
        new_value : felt)
