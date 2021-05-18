Common Library
==============

This page summarizes library functions available within Cairo.

The library functions are arranged alphabetically and cover the
following topics:

- dictionary
    - :ref:`common_library_dict_access`
    - :ref:`common_library_dict`
    - :ref:`common_library_default_dict`
    - :ref:`common_library_squash_dict`
- array
    - :ref:`common_library_find_element`
- math
    - :ref:`common_library_math`
- hash
    - :ref:`common_library_hash`
    - :ref:`common_library_hash_chain`
    - :ref:`common_library_hash_state`
    - :ref:`common_library_small_merkle_tree`
    - :ref:`common_library_merkle_update`
    - :ref:`common_library_merkle_multi_update`
- signature
    - :ref:`common_library_signature`
- memory and state
    - :ref:`common_library_alloc`
    - :ref:`common_library_registers`
    - :ref:`common_library_cairo_builtins`
    - :ref:`common_library_memcpy`
    - :ref:`common_library_serialize`

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

Verifies that value != 0. The proof will fail otherwise.

.. tested-code:: cairo library_assert_not_zero

    assert_not_zero(value)

``assert_not_equal()`` function
*******************************

Verifies that a != b. The proof will fail otherwise.

.. tested-code:: cairo library_assert_not_equal

    assert_not_zero(a, b)

``assert_nn()`` function
************************

Verifies that a >= 0 (or more precisely 0 <= a < RANGE_CHECK_BOUND).
Informally, that a is non-negative ("nn"). The proof will fail
otherwise. The function requires the implicit argument
``range_check_ptr``.

.. tested-code:: cairo library_assert_nn

    assert_nn(a):

``assert_le()`` function
************************

Verifies that a <= b (or more precisely 0 <= b - a < RANGE_CHECK_BOUND).
Informally, that a is less than or equal to ("le") b. The proof will
fail otherwise. The function requires the implicit argument
``range_check_ptr``.

.. tested-code:: cairo library_assert_le

    assert_le(a, b)

``assert_lt()`` function
************************

# Verifies that a <= b - 1 (or more precisely 0 <= b - 1 - a <
RANGE_CHECK_BOUND). Informally, the a is less than ("lt") b. The proof
will fail otherwise. The function requires the implicit argument
``range_check_ptr``.

.. tested-code:: cairo library_assert_lt

    assert_lt(a, b)

``assert_nn_le()`` function
***************************

Verifies that 0 <= a <= b. Informally that a and b are non-negative
("nn") and that a is less than or equal to b. The proof will fail
otherwise. The function requires the implicit argument
``range_check_ptr``.

.. tested-code:: cairo library_assert_nn_le

    assert_nn_le(a, b)

``assert_in_range()`` function
******************************

Verifies that value is in the range [lower, upper). Informally, that
value is both greater than or equal to lower and less than upper. The
proof will fail otherwise. The function requires the implicit argument
``range_check_ptr``.

.. tested-code:: cairo library_assert_in_range

    assert_in_range(value, upper, lower)

``assert_le_250_bit()`` function
********************************

Verifies that a and b are in the range [0, 2**250). Informally, that
both a and b are non-negative and less that the largest number possible
in a binary system with 250 bits. The proof will fail otherwise. The
function requires the implicit argument ``range_check_ptr``.

.. tested-code:: cairo library_assert_le_250_bit

    assert_le_250_bit(a, b)

``split_felt()`` function
*************************

Splits the unsigned integer lift of a field element into the higher 128
bit and lower 128 bit and returns both numbers. The unsigned integer
lift is the unique integer in the range [0, PRIME) that represents the
field element.

Informally, the function accepts a value and returns two numbers that
uniquely represent that value within the field element system that
Cairo uses.

For example, if ``value`` = 17 * 2^128 + 8, then ``high`` = 17 and
``low`` = 8.

The function requires the implicit argument ``range_check_ptr``.

.. tested-code:: cairo library_split_felt

    let (high, low) = split_felt(value)

``assert_le_felt()`` function
*****************************

Verifies that the unsigned integer lift (as a number in the range
[0, PRIME)) of a is lower than or equal to that of b. Informally,
that the integer of the larger component of the field element is less
than the integer of the smaller component. The proof will fail
otherwise. The function requires the implicit argument
``range_check_ptr``.

For example, the proof for assert_le_felt(17 * 2^128 + 8) would faile
because because 17>8.

.. tested-code:: cairo library_assert_le_felt

    assert_le_felt(value)

``abs_value()`` function
************************

Returns the absolute value of a value. Informally, the function returns
the value provided with any negative sign removed. The function requires
the implicit argument ``range_check_ptr``.


.. tested-code:: cairo library_abs_value

    abs_value(value)

``sign()`` function
*******************

Returns the sign of value: -1, 0 or 1. Informally, for positive numbers
the function returns 1, for negative numbers the function returns -1 and
for zero the function returns 0. The function requires the implicit
argument ``range_check_ptr``.

.. tested-code:: cairo library_sign

    let value_sign = sign(value)

``unsigned_div_rem()`` function
*******************************

Returns q and r such that 0 <= q < rc_bound, 0 <= r < div and value
= q * div + r. Informally, the function returns the quotient and
remainder for a value and divisor, ignoring negative values. The
function requires the implicit argument ``range_check_ptr``.

.. tested-code:: cairo library_unsigned_div_rem

    let (unsigned_quotient, remainder) = unsigned_div_rem(value, divisor)

``signed_div_rem()`` function
*****************************

Returns q and r such that 0 <= q < rc_bound, 0 <= r < div and value
= q * div + r. Informally, the function returns the quotient and
remainder for a value and divisor, ignoring negative values. The
function requires the implicit argument ``range_check_ptr``.

.. tested-code:: cairo library_signed_div_rem

    let (signed_quotient, remainder) = unsigned_div_rem(value, divisor)

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
