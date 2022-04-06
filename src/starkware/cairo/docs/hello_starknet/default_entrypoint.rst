Default entry point
===================

There are cases where the contract entry points are not known in advance.
The most prominent example is a delegate proxy that forwards calls to an implementation
contract.
Such a proxy can be implemented using the ``__default__`` entry point as follows:

.. tested-code:: cairo delegate_proxy

    %lang starknet
    %builtins pedersen range_check bitwise

    from starkware.cairo.common.cairo_builtins import HashBuiltin
    from starkware.starknet.common.syscalls import delegate_call

    # The address of the implementation contract.
    @storage_var
    func impl_address() -> (address : felt):
    end

    @external
    func constructor{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(impl_address_ : felt):
        impl_address.write(value=impl_address_)
        return ()
    end

    @external
    @raw_input
    @raw_output
    func __default__{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(selector : felt, calldata_size : felt, calldata : felt*) -> (
        retdata_size : felt, retdata : felt*
    ):
        let (address) = impl_address.read()

        let (retdata_size : felt, retdata : felt*) = delegate_call(
            contract_address=address,
            function_selector=selector,
            calldata_size=calldata_size,
            calldata=calldata,
        )
        return (retdata_size=retdata_size, retdata=retdata)
    end

The ``__default__`` entry point is executed if the requested selector does not match any of the
entry point selectors in the contract.

The ``@raw_input`` decorator instructs the compiler to pass the calldata
as-is to the entry point, instead of parsing it into the requested arguments.
In such a case, the function's arguments must be
``selector``, ``calldata_size`` and ``calldata``.
Similarly, the ``@raw_output`` decorator instructs the compiler not to process
the function's return value.
In such a case the function's return values must be ``retdata_size`` and ``retdata``.

In a similar way to ``__default__``, the ``__l1_default__`` entry point that is executed when an L1
handler is invoked but the requested selector is missing. This entry point in combination with the
``delegate_l1_handler`` system call can be used to forward L1 handlers as follows:

.. tested-code:: cairo delegate_l1_handler

    from starkware.starknet.common.syscalls import (
        delegate_l1_handler,
    )

    @l1_handler
    @raw_input
    func __l1_default__{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(selector : felt, calldata_size : felt, calldata : felt*):
        let (address) = impl_address.read()

        delegate_l1_handler(
            contract_address=address,
            function_selector=selector,
            calldata_size=calldata_size,
            calldata=calldata,
        )
        return ()
    end

The ``delegate_l1_handler`` system call is similar to the delegate_call except that it invokes an
``l1_handler`` entry point instead of an ``external`` entry point.
The system call does not consume an L1 -> L2 message as in the typical use case, the relevant
message is consumed by the l1_handler that issued the system call.
Furthermore, this system call cannot be used to trick the called contract into accepting a 'fake'
L1 -> L2 message, as the entry point is executed in the context of the calling contract, rather than
the context of the called contract.
