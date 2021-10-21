.. proofedDate:: null

.. comment:: null

.. toctree::
   :maxdepth: 2
   :caption: Contents:

More Features
=============

Storage variable with multiple values
-------------------------------------

A storage variable does not have to be a single field element,
it can also be a tuple of several field elements.
For example:

.. tested-code:: cairo storage_var_range

    # A mapping from user to a pair (min, max).
    @storage_var
    func range(user : felt) -> (res : (felt, felt)):
    end

You can read and write this value as follows:

.. tested-code:: cairo extend_range

    @external
    func extend_range{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(user : felt):
        let (min_max) = range.read(user)
        range.write(user, (min_max[0] - 1, min_max[1] + 1))
        return ()
    end

Note that in this case the ``range.read()`` returns one item that is a pair.
Thus, ``let (min, max) = range.read(user)`` will not work.

Array arguments in calldata
---------------------------

An external function may get an array of field elements as an argument.
In order to define an array named ``a``, pass two consecutive arguments:
``a_len`` of type ``felt`` and ``a`` of type ``felt*``
(the first argument *must* be named ``a_len`` if the second argument is named ``a``).
For example:

.. tested-code:: cairo compare_arrays

    @external
    func compare_arrays(
            a_len : felt, a : felt*, b_len : felt, b : felt*):
        assert a_len = b_len
        if a_len == 0:
            return ()
        end
        assert a[0] = b[0]
        return compare_arrays(
            a_len=a_len - 1, a=a + 1, b_len=b_len - 1, b=b + 1)
    end

In order to call ``compare_arrays`` with the arrays ``[10, 20, 30, 40]`` and ``[50, 60]``,
you should pass the following inputs to ``starknet invoke``:

.. tested-code:: bash invoke_compare_arrays

    starknet invoke \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function compare_arrays \
        --inputs 4 10 20 30 40 2 50 60

The first value, 4, is the length of the first array,
then its 4 entires. After that, we have the length of the second arrays (2) followed by
its entries.
Note that calling ``compare_arrays`` with the aforementioned
arguments will fail as the arrays are different.

A StarkNet contract using array arguments in external functions
must have the range_check builtin, which is used
to validate that the array's length is nonnegative.
