
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
create dictionaries where all keys have the same value (``default_value``).
The dictionary can be initialised using a hint with the special ``initial_dict``
expression declaring a dictionary.

The function requires one explicit argument:

-   ``default_value``, a ``felt`` that will be set for all keys.

The function returns:

-   ``res``, a pointer to a ``DictAccess`` struct.

In the code below, an empty default dictionary is made and finalized.
The values provided in the hint are replaced by the default value.

.. tested-code:: cairo library_default_dict_new

    from starkware.cairo.common.default_dict import default_dict_new

    alloc_locals
    # Hint to initialise the dictionary
    %{
        initial_dict = {
        17: 35,
        57: 9
        }
    %}
    # Create a new default dict. Values are overriden by "7".
    # Initial dictionary: {17: 7, 57: 7}.
    let (local my_dict) = default_dict_new(7)
    # Dictionary must be now finalized
    # with a call to default_dict_finalize()

``default_dict_finalize()``
***************************

Returns the squashed version of a default dictionary. The function is
used to remove the intermediate dictionary states. All updates to the dictionary
are sequentially applied and a new dictionary is returned with the final values.
The value of ``default_value`` in the original call to ``default_dict_new()`` is
checked ensure it matches that supplied in this function call.

The function requires three explicit arguments:

-   ``dict_accesses_start``, a pointer ``DictAccess*``, to the initial value of the dictionary.
-   ``dict_accesses_end``, a pointer ``DictAccess*``, to the latest value of the dictionary.
-   ``default_value``, the default value specified when this dictionary was created.

The function returns:

-   ``squashed_dict_start``, a pointer to the initial state of the dictionary.
-   ``squashed_dict_end``, a pointer to the final state of the dictionary.

The code below is the missing code from the example in ``default_dict_new``.
The value of ``val`` is trusted because it is after the function that finalizes
the dictionary, which verifies that the default values were applied.

.. tested-code:: cairo library_default_dict_finalize

    from starkware.cairo.common.default_dict import (
        default_dict_finalize)
    from starkware.cairo.common.dict import dict_read

    # Code that creates the default dict here.
    # Finalize dict, ensuring that the initial values are all "7".
    let (local old, my_dict_final) = default_dict_finalize(
        my_dict, my_dict, 7)
    # Equivalent to: let val = 7.
    let (local val : felt) = dict_read{dict_ptr=my_dict_final}(57)