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
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(user : felt):
        let (min_max) = range.read(user)
        range.write(user, (min_max[0] - 1, min_max[1] + 1))
        return ()
    end

Note that in this case the ``range.read()`` returns one item that is a pair.
Thus, ``let (min, max) = range.read(user)`` will not work.

Storage variable with struct arguments
--------------------------------------

An argument of a storage variable may also be a struct or a tuple, as long as
they don't contain pointers (such types, that don't contain pointers, are called felts-only types).
For example:

.. tested-code:: cairo storage_var_struct

    struct User:
        member first_name : felt
        member last_name : felt
    end

    # A mapping from a user to 1 if they voted and 0 otherwise.
    @storage_var
    func user_voted(user : User) -> (res : felt):
    end

    @external
    func vote{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(user : User):
        user_voted.write(user, 1)
        return ()
    end

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
        a_len : felt, a : felt*, b_len : felt, b : felt*
    ):
        assert a_len = b_len
        if a_len == 0:
            return ()
        end
        assert a[0] = b[0]
        return compare_arrays(
            a_len=a_len - 1, a=&a[1], b_len=b_len - 1, b=&b[1]
        )
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

Passing tuples and structs in calldata
--------------------------------------

Calldata arguments and return values may be of any type that does not contain pointers.
E.g., structs with felt members, tuples of felts and tuples of tuples of felts.
For example:

.. tested-code:: cairo sum_points

    struct Point:
        member x : felt
        member y : felt
    end

    @view
    func sum_points(points : (Point, Point)) -> (res : Point):
        return (
            res=Point(
            x=points[0].x + points[1].x,
            y=points[0].y + points[1].y),
        )
    end

In order to call ``sum_points`` with the points ``(1, 2), (10, 20)``,
you should pass the following inputs to ``starknet call``:

.. tested-code:: bash call_sum_points

    starknet call \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function sum_points \
        --inputs 1 2 10 20

Passing arrays of structs
-------------------------

In a similar way, passing arrays of structs is supported,
as long as the structs do not contain pointers:

.. tested-code:: cairo sum_points_arr

    @external
    func sum_points_arr(a_len : felt, a : Point*) -> (res : Point):
        if a_len == 0:
            return (Point(0, 0))
        end
        let (res) = sum_points_arr(a_len=a_len - 1, a=&a[1])
        return (res=Point(x=res.x + a[0].x, y=res.y + a[0].y))
    end

In order to call ``sum_points_arr`` with the 3 points ``(1, 2), (10, 20), (100, 200)``,
you should pass the following inputs to ``starknet call``:

.. tested-code:: bash call_sum_points_arr

    starknet call \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function sum_points_arr \
        --inputs 3 1 2 10 20 100 200

Retrieving the transaction information
--------------------------------------

You can retrieve the transaction information
(which includes, for example, the signature and the transaction fee),
by using the ``get_tx_info()`` library function:

.. tested-code:: cairo get_tx_info_example

    from starkware.starknet.common.syscalls import get_tx_info

    func get_tx_max_fee{syscall_ptr : felt*}() -> (max_fee : felt):
        let (tx_info) = get_tx_info()

        return (max_fee=tx_info.max_fee)
    end

The returned value is a pointer to a ``TxInfo`` struct, which is defined as follows:

.. tested-code:: cairo get_tx_info_struct

    struct TxInfo:
        # The version of the transaction. It is fixed (currently, 0) in the OS, and should be
        # signed by the account contract.
        # This field allows invalidating old transactions, whenever the meaning of the other
        # transaction fields is changed (in the OS).
        member version : felt

        # The account contract from which this transaction originates.
        member account_contract_address : felt

        # The max_fee field of the transaction.
        member max_fee : felt

        # The signature of the transaction.
        member signature_len : felt
        member signature : felt*

        # The hash of the transaction.
        member transaction_hash : felt

        # The identifier of the chain.
        # This field can be used to prevent replay of testnet transactions on mainnet.
        member chain_id : felt
    end

Block number and timestamp
--------------------------

You can get the current block number and timestamp (seconds since unix epoch) by using the
``get_block_number()`` and ``get_block_timestamp()`` library functions.

.. tested-code:: cairo get_block_params

    from starkware.starknet.common.syscalls import (
        get_block_number,
        get_block_timestamp,
    )

    # ...

    let (block_number) = get_block_number()
    let (block_timestamp) = get_block_timestamp()

Note that both of the above functions require the implicit argument ``syscall_ptr``. Presently, the
result of ``get_block_timestamp()`` is not enforced by the StarkNet OS or Core contract (i.e., the
sequencer may choose an arbitrary timestamp). In the future, some restrictions on the new timestamp
will be added. Also note that the block timestamp is the time at the beginning of the
block creation, which can differ significantly from the time the block is accepted on L1.

.. test::

    from starkware.cairo.lang.compiler.cairo_compile import compile_cairo
    from starkware.cairo.lang.cairo_constants import DEFAULT_PRIME
    from starkware.python.utils import get_source_dir_path

    # Make sure the code compiles.
    compile_cairo(codes["get_tx_info_example"], prime=DEFAULT_PRIME)

    syscalls_file_path = get_source_dir_path("src/starkware/starknet/common/syscalls.cairo")
    assert codes["get_tx_info_struct"] in open(syscalls_file_path).read(), \
        "Please update 'get_tx_info_struct' code segment to match the struct in syscalls.cairo."
