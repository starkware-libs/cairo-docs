
``dict_update()``
*****************

Updates the value of a particular key in a dictionary. The old value must be provided and
passed an implicit argument, ``DictAccess*``, a pointer to the most recent dictionary access.
No values are returned.

.. tested-code:: cairo library_dict_update

    from starkware.cairo.common.dict import dict_update

    dict_update{dict_ptr : DictAccess*}(
        key : felt,
        prev_value : felt,
        new_value : felt)

``dict_squash()``
*****************

Returns a dictionary that represents the the final state of an altered dictionary.
A dictionary that has been updated and that has had all intermediate steps removed.
The squashed dictionary contains one value per key. The function requires
``range_check_pointer`` as an implicit argument.

.. tested-code:: cairo library_dict_squash

    from starkware.cairo.common.dict import dict_squash

    let (squashed_dict_start, squashed_dict_end) = dict_squash(
        dict_accesses_start : DictAccess*
        dict_accesses_end : DictAccess*)

``dict_access``
---------------

This section contains a struct from the ``dict_access`` library.

``DictAccess``
**************

Returns a new struct that is used in other dictionary-related functions.

.. tested-code:: cairo library_dictaccess

from starkware.cairo.common.dict_access import DictAccess

    alloc_locals
    local (new_dict : DictAccess)
