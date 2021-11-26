.. _calling_contracts:


Calling another contract
========================

A contract function may invoke an external function of another contract.

Start by deploying the example contract in :ref:`starknet_intro`
(the compilation and deployment instructions can be found at
:ref:`the bottom of the page <compile_contract>`).
Denote the address of this contract by ``BALANCE_CONTRACT``.

In order to call this contract from another contract, define an interface
by copying the declarations of the external functions:

.. tested-code:: cairo call_contract_interface

    @contract_interface
    namespace IBalanceContract:
        func increase_balance(amount : felt):
        end

        func get_balance() -> (res : felt):
        end
    end

Note that the body of the functions and the implicit arguments should be removed
from the definitions.

You can use ``IBalanceContract.increase_balance()`` and ``IBalanceContract.get_balance()``
to invoke these functions on another contract.
For example:

.. tested-code:: cairo call_contract_code

    @external
    func call_increase_balance{syscall_ptr : felt*, range_check_ptr}(
            contract_address : felt, amount : felt):
        IBalanceContract.increase_balance(
            contract_address=contract_address, amount=amount)
        return ()
    end

    @view
    func call_get_balance{syscall_ptr : felt*, range_check_ptr}(
            contract_address : felt) -> (res : felt):
        let (res) = IBalanceContract.get_balance(
            contract_address=contract_address)
        return (res=res)
    end

Note that calling a function of another contract requires passing one additional argument
before the function's original arguments -- the address of the called contract.
For example, ``IBalanceContract.increase_balance`` gets two arguments:
``contract_address`` and ``amount`` (rather than just ``amount``).
In addition, the ``syscall_ptr`` and the ``range_check_ptr`` implicit arguments
are required.

Create a file named ``proxy_contract.cairo`` containing the interface declaration and the two
functions ``call_increase_balance()`` and ``call_get_balance()``,
and deploy the contract.
Denote the address of the new contract by ``PROXY_CONTRACT``.

Now, invoke ``call_increase_balance`` with ``BALANCE_CONTRACT``
as the value of the ``contract_address`` argument.
Make sure you replace ``PROXY_CONTRACT`` and ``BALANCE_CONTRACT``
with the addresses you got when you deployed the two contracts:

.. tested-code:: bash invoke_call_increase_balance

    starknet invoke \
        --address PROXY_CONTRACT \
        --abi proxy_contract_abi.json \
        --function call_increase_balance \
        --inputs BALANCE_CONTRACT 10000

This will increase the balance stored in ``BALANCE_CONTRACT``.
Note that in our case, ``PROXY_CONTRACT`` does not have a storage of its own.

Wait until the transaction is added to a block, and then
check the balance using the following two ways:

1.  Directly through ``BALANCE_CONTRACT``

    .. tested-code:: bash calling_contracts_get_balance_a

        starknet call \
            --address BALANCE_CONTRACT \
            --abi balance_contract_abi.json \
            --function get_balance

2.  Indirectly through ``PROXY_CONTRACT``

    .. tested-code:: bash calling_contracts_get_balance_b

        starknet call \
            --address PROXY_CONTRACT \
            --abi proxy_contract_abi.json \
            --function call_get_balance \
            --inputs BALANCE_CONTRACT

Both commands should return ``10000``.

Getting the caller address
--------------------------

You can retrieve the address of the contract that invoked your function
(if the function was called by another contract)
using the ``get_caller_address()`` library function:

.. tested-code:: cairo get_caller_address

    from starkware.starknet.common.syscalls import get_caller_address

    # ...

    let (caller_address) = get_caller_address()

When the contract is called by a user (rather than another contract),
the function returns 0.

Consider what would happen if you added a call to ``get_caller_address()``
to the ``increase_balance()`` function of ``BALANCE_CONTRACT``:
It would return ``PROXY_CONTRACT`` if called from
``PROXY_CONTRACT``, and 0 if called directly.

Note that if you use ``get_caller_address()`` in a function ``foo()`` that was called by
another function ``bar()`` within your contract,
it will still return the address of the contract that invoked ``bar()``
(or 0 if it was invoked by a user).

Getting the current contract's address
--------------------------------------

You can get the current contract's address by using the ``get_contract_address()`` library function.

.. tested-code:: cairo get_contract_address

    from starkware.starknet.common.syscalls import (
        get_contract_address)

    # ...

    let (contract_address) = get_contract_address()

The above is similar to ``address(this)`` in Solidity.
