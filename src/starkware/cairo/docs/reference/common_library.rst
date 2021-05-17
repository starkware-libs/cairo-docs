Common Library
==============

This page summarizes library functions available within Cairo. 

Where a library function requires an implicit argument, passing the 
argument is only required if the function lacks that argument. Example
implicit arguments might be ``range_check_ptr`` or ``dict_ptr``.

.. tested-code:: cairo library_implicits0

    # Implicit argument part of function
    function{implicit_argument}():
        # Implicit argument not required again
        library_function()

.. tested-code:: cairo library_implicits1

    # Implicit argument not part of function
    function():
        # Implicit argument required
        library_function{implicit_argument}()

``alloc`` library
-----------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_alloc

    from starkware.cairo.common.alloc import *

``alloc()`` function
********************

Returns a newly allocated memory segment.

.. tested-code:: cairo alloc_alloc

    let new_slot = alloc()

.. _common_library_alloc:

``cairo_builtins`` library
--------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_cairo_builtins

    from starkware.cairo.common.cairo_builtins import *

``HashBuiltin`` function
************************

Returns a representation of a ``HashBuiltin struct``, specifying the 
hash builtin memory structure.

.. tested-code:: cairo library_builtins_hashbuiltin

    alloc_locals
    local new_hash : HashBuiltin

``SignatureBuiltin`` function
*****************************
    
Returns a representation of a ``SignatureBuiltin struct``, specifying 
the signature builtin memory structure.

.. tested-code:: cairo library_builtins_signaturebuiltin

      alloc_locals
      local new_signature : SignatureBuiltin

``CheckpointsBuiltin`` function
*******************************
    
Returns a representation of a ``CheckpointsBuiltin struct``, specifying 
the checkpoint builtin memory structure.

.. tested-code:: cairo library_builtins_checkpointsbuiltin

      alloc_locals
      local new_checkpoint : CheckpointsBuiltin

.. _common_library_cairo_builtins:

``default_dict`` library
------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_default_dict

    from starkware.cairo.common.default_dict import *

``default_dict_new()`` function
*******************************

Returns a new dictionary, with a default value. Must be followed by a 
call to ``default_dict_finalize()``.

.. tested-code:: cairo library_default_dict_new

    let new_dictionary = default_dict_new(value: felt)

``default_dict_finalize()`` function
************************************

Returns the squashed version of a ``default_dict_new`` dictionary.

.. tested-code:: cairo library_default_dict_finalize

    let finalized_dictionary = default_dict_finalize(new_dictionary)

.. _common_library_default_dict:

``dict`` library
----------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_dict

    from starkware.cairo.common.dict import *

``dict_new()`` function
***********************

Returns a new dictionary.

.. tested-code:: cairo library_dict_new

    let new_dict = new_dict()


``dict_read()`` function
************************

Returns the value of a dictionary read. Must be passed an implicit 
argument pointing to the most recent version of the dictionary.

.. tested-code:: cairo library_dict_read

    let result = dict_read{dict_ptr : DictAccess*}(dict_key)

``dict_write()`` function
*************************

Writes a value to the dictionary, overriding the existing value. Must 
be passed an implicit argument pointing to the most recent version of 
the dictionary. No values are returned. 

.. tested-code:: cairo library_dict_write

    dict_write{dict_ptr : DictAccess*}(
        key : felt, 
        new_value : felt)

``dict_update()`` function
**************************

Updates the value of a particular key in a dictionary. The old value 
must be provided. Must be passed an implicit argument pointing to 
the most recent version of the dictionary. No values are returned.

.. tested-code:: cairo library_dict_update

    dict_update{dict_ptr : DictAccess*}(
        key : felt, 
        prev_value : felt, 
        new_value : felt)

``dict_squash()`` function
**************************

Returns a dictionary that represents the the final state of an altered
dictionary. A dictionary that has been updated and that has had all 
intermediate steps removed. The squashed dict contains one value per 
key. The function requires a range check pointer as an implicit 
argument.

.. tested-code:: cairo library_dict_squash

    let (squashed_dict_start, squashed_dict_end) = dict_squash(
        dict_accesses_start : DictAccess*
        dict_accesses_end : DictAccess*)
    
.. _common_library_dict:


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

.. _common_library_dict_access:

``find_element`` library
------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_find_element

    from starkware.cairo.common.find_element import *

``find_element()`` function
***************************

Returns TODO

.. tested-code:: cairo library_find_element

    TODO

``search_sorted_lower()`` function
**********************************

Returns TODO

.. tested-code:: cairo library_search_sorted_lower

    TODO

``search_sorted()`` function
****************************

Returns TODO

.. tested-code:: cairo library_search_sorted

    TODO

.. _common_library_find_element:


``hash`` library
----------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_hash

    from starkware.cairo.common.hash import *

``hash2()`` function
********************

Returns TODO

.. tested-code:: cairo library_hash2

    TODO

.. _common_library_hash:

``hash_chain`` library
----------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_hash_chain

    from starkware.cairo.common.hash_chain import *

``hash_chain()`` function
*************************

Returns TODO

.. tested-code:: cairo library_hash_chain

    TODO

.. _common_library_chain:

``hash_state`` library
----------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_hash_state

    from starkware.cairo.common.hash_state import *

``hash_init()`` function
************************

Returns TODO

.. tested-code:: cairo library_hash_init

    TODO

``hash_update()`` function
**************************

Returns TODO

.. tested-code:: cairo library_hash_update

    TODO

``hash_update_single()`` function
*********************************

Returns TODO

.. tested-code:: cairo library_hash_update_single

    TODO
    
.. _common_library_hash_state:

``math`` library
----------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_math

    from starkware.cairo.common.math import *

``assert_not_zero()`` function
******************************

Returns TODO

.. tested-code:: cairo library_assert_not_zero

    TODO

``assert_not_equal()`` function
*******************************

Returns TODO

.. tested-code:: cairo library_assert_not_equal

    TODO

``assert_nn()`` function
************************

Returns TODO

.. tested-code:: cairo library_assert_nn

    TODO

``assert_le()`` function
************************

Returns TODO

.. tested-code:: cairo library_assert_le

    TODO

``assert_lt()`` function
************************

Returns TODO

.. tested-code:: cairo library_assert_lt

    TODO

``assert_nn_le()`` function
***************************

Returns TODO

.. tested-code:: cairo library_assert_nn_le

    TODO

``assert_in_range()`` function
******************************

Returns TODO

.. tested-code:: cairo library_assert_in_range

    TODO

``assert_le_250_bit()`` function
********************************

Returns TODO

.. tested-code:: cairo library_assert_le_250_bit

    TODO

``split_felt()`` function
*************************

Returns TODO

.. tested-code:: cairo library_split_felt

    TODO

``assert_le_felt()`` function
*****************************

Returns TODO

.. tested-code:: cairo library_assert_le_felt

    TODO

``abs_value()`` function
************************

Returns TODO

.. tested-code:: cairo library_abs_value

    TODO

``sign()`` function
*******************

Returns TODO

.. tested-code:: cairo library_sign

    TODO

``unsigned_div_rem()`` function
*******************************

Returns TODO

.. tested-code:: cairo library_unsigned_div_rem

    TODO

``signed_div_rem()`` function
*****************************

Returns TODO

.. tested-code:: cairo library_signed_div_rem

    TODO

.. _common_library_math:

``memcpy`` library
------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_memcpy0

    from starkware.cairo.common.memcpy import *

``memcpy()`` function
*********************

Returns TODO

.. tested-code:: cairo library_memcpy1

    TODO

.. _common_library_memcpy:

``merkle_multi_update`` library
-------------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_merkle_multi_update0

    from starkware.cairo.common.merkle_multi_update import *

``merkle_multi_update()`` function
**********************************

Returns TODO

.. tested-code:: cairo library_merkle_multi_update1

    TODO

.. _common_library_merkle_multi_update:

``merkle_update`` library
-------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_merkle_update

    from starkware.cairo.common.merkle_update import *

``merkle_update()`` function
****************************

Returns TODO

.. tested-code:: cairo library_merkle_update

    TODO

.. _common_library_merkle_update:

``registers`` library
---------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_registers

    from starkware.cairo.common.registers import *

``get_fp_and_pc()`` function
****************************

Returns TODO

.. tested-code:: cairo library_get_fp_and_pc

    TODO

``get_ap()`` function
*********************

Returns TODO

.. tested-code:: cairo library_get_ap

    TODO
    
``get_label_location()`` function
*********************************

Returns TODO

.. tested-code:: cairo library_get_label_location

    TODO

.. _common_library_registers:

``serialize`` library
---------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_serialize

    from starkware.cairo.common.serialize import *

``serialize_word()`` function
*****************************

Returns TODO

.. tested-code:: cairo library_serialize_word

    TODO

``array_rfold()`` function
**************************

Returns TODO

.. tested-code:: cairo library_array_rfold

    TODO

``serialize_array()`` function
******************************

Returns TODO

.. tested-code:: cairo library_serialize_array

    TODO

.. _common_library_serialize:

``signature`` library
---------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_signature

    from starkware.cairo.common.signature import *

``verify_ecdsa_signature()`` function
*************************************

Returns TODO

.. tested-code:: cairo library_verify_ecdsa_signature

    TODO

.. _common_library_signature:

``small_merkle_tree`` library
-----------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_small_merkle_tree

    from starkware.cairo.common.small_merkle_tree import *

``small_merkle_tree()`` function
********************************

Returns TODO

.. tested-code:: cairo library_small_merkle_tree

    TODO

``merkle_multi_update()`` function
**********************************

Returns TODO

.. tested-code:: cairo library_merkle_multi_update

    TODO

.. _common_library_small_merkle_tree:

``squash_dict`` library
-----------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_squash_dict

    from starkware.cairo.common.squash_dict import *

``squash_dict()`` function
**************************

Returns TODO

.. tested-code:: cairo library_squash_dict

    TODO

.. _common_library_squash_dict:
