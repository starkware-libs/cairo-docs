
``dict``
--------

This section contains functions from the ``dict`` library.

``dict_new()``
**************

Returns a new dictionary. The function does not require any arguments.
A new dictionary can be populated upon declaration by using a hint with with the
expression ``initial_dict``. The dictionary associated with that expression
will be found by the ``__dict_manager`` and assigned to the new dictionary.

The function returns one argument:

-   ``res``, a pointer to a ``DictAccess`` element.

.. tested-code:: cairo library_dict_new

    from starkware.cairo.common.dict import dict_new
    from starkware.cairo.common.dict_access import DictAccess

    let new_dict = new_dict()

    alloc_locals
    %{
        initial_dict = {
            5: 8,
            12: 35,
            33: 198
        }
    %}
    # Equivalent to: my_dict = {5: 8, 12: 35, 33: 198}
    let (local my_dict : DictAccess*) = dict_new()

``dict_read()``
***************

Returns the value of a dictionary read. Must be passed an implicit argument, ``dict_ptr``,
of type ``DictAccess*``, representing a pointer to the dictionary from which to be read.

The function accepts one explicit argument:

-   ``key``, a ``felt`` representing the key of a key-value pair.

The function returns:

-   ``value``, a ``felt`` representing the value assigned to ``key``.

The example below shows how a value can be read from a newly created dictionary.

.. tested-code:: cairo library_dict_read

    from starkware.cairo.common.dict import dict_new, dict_read
    from starkware.cairo.common.dict_access import DictAccess

    alloc_locals
    %{
        initial_dict = {
        5: 8,
        12: 35,
        33: 198
        }
    %}
    let (local a_dict : DictAccess*) = dict_new()
    # The pointer, dict_a, is passed as an implicit argument.
    # The value associated with key=12 is read.
    # Equivalent to: local val = 35
    let (local val : felt) = dict_read{dict_ptr=a_dict}(12)

``dict_write()``
****************

Writes a value to the dictionary, overriding the existing value. Must be passed an
implicit argument, ``dict_ptr``, of type ``DictAccess*``, representing a pointer
to the dictionary in which to write. No values are returned.

The function accepts two explicit arguments:

-   ``key``, a ``felt`` representing the key of a key-value pair.
-   ``new_value``, a ``felt`` that will overwrite the existing value of a key-value pair.

.. tested-code:: cairo library_dict_write

    from starkware.cairo.common.dict import (
        dict_new, dict_read, dict_write)
    from starkware.cairo.common.dict_access import DictAccess

    alloc_locals
    %{
        initial_dict = {
        5: 8,
        12: 35,
        33: 198
        }
    %}
    let (local a_dict : DictAccess*) = dict_new()
    # The pointer, dict_a, is passed as an implicit argument.
    # The value associated with key=12 is set to 34.
    dict_write{dict_ptr=a_dict}(12, 34)
    # Equivalent to: local val = 34 (35 was overwritten)
    let (local val : felt) = dict_read{dict_ptr=a_dict}(12)
