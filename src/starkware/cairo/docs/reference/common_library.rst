
``dict``
--------

This section contains functions from the ``dict`` library.

``dict_new()``
**************

Returns a new dictionary. The function does not require any arguments.

The function returns one argument:

-   ``res``, a pointer to a ``DictAccess`` element.

.. tested-code:: cairo library_dict_new

    from starkware.cairo.common.dict import dict_new

    let new_dict = new_dict()

``dict_read()``
***************

Returns the value of a dictionary read. Must be passed an implicit argument, ``dict_ptr``,
 of type ``DictAccess*``, representing a pointer to the dictionary from which to be read.

The function accepts one explicit argument:

-   ``key``, a ``felt`` representing the key of a key-value pair.

The function returns:

-   ``value``, a ``felt`` representing the value assigned to ``key``.

.. tested-code:: cairo library_dict_read

    from starkware.cairo.common.dict import dict_read

    let result = dict_read{dict_ptr : DictAccess*}(dict_key)

``dict_write()``
****************

Writes a value to the dictionary, overriding the existing value. Must be passed an
implicit argument, ``dict_ptr``, of type ``DictAccess*``, representing a pointer
to the dictionary in which to write. No values are returned.

The function accepts two explicit arguments:

-   ``key``, a ``felt`` representing the key of a key-value pair.
-   ``new_value``, a ``felt`` that will overwrite the existing value of a key-value pair.

.. tested-code:: cairo library_dict_write

    from starkware.cairo.common.dict import dict_write

    dict_write{dict_ptr : DictAccess*}(
        key : felt,
        new_value : felt)
