
``dict_update()`` function
**************************

Updates the value of a particular key in a dictionary. The old value must be provided. Must be
passed an implicit argument pointing to the most recent version of the dictionary. No values are
returned.

.. tested-code:: cairo library_dict_update

    dict_update{dict_ptr : DictAccess*}(
        key : felt,
        prev_value : felt,
        new_value : felt)

``dict_squash()`` function
**************************

Returns a dictionary that represents the the final state of an altered dictionary. A dictionary that
has been updated and that has had all intermediate steps removed. The squashed dict contains one
value per key. The function requires a range check pointer as an implicit argument.

.. tested-code:: cairo library_dict_squash

    let (squashed_dict_start, squashed_dict_end) = dict_squash(
        dict_accesses_start : DictAccess*
        dict_accesses_end : DictAccess*)

``dict_access`` library
-----------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_dict_access

    from starkware.cairo.common.dict_access import *

``DictAccess`` function
***********************

Returns a new struct that is used in other dictionary-related functions

.. tested-code:: cairo library_dictaccess

    alloc_locals
    local (new_dict : DictAccess)
