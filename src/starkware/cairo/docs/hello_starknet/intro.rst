.. proofedDate null

.. comment Restructure suggested. toc/overview will assist in page breakdown and nav.

.. suggestedEdits1 {wip The @storage_var decorator declares a variable that will be kept as part of this storage}> Consider [The @storage_var decorator declares which variables will be stored.]

.. suggestedEdits2 {wip If you want to restrict it,} > This is weaving around the matter. Consider [Restrictions and authentication requirements can be implemented using the ecdsa builtin](note I exclude the user's signature part as I believe this is covered by "authentication") ALT Split it [Suppose you want to restrict user access to external functions, or enforce authentication. In that case, you can use the edca ...]

.. suggestedEdits3 {wip Note that in the current version, this is not enforced by the compiler.} What is not enforced -- that a method may only annotate? Consider clarifying [or explaining to me, so that I can clarify]

.. suggestedEdits4 {wip Note that in our PC world, whitelisting is being slain (along with the master branch). If you want to be PC the term is allow-list} > Please confirm yes/no to change and I can apply.

.. _starknet_intro:

Writing StarkNet Contracts
==========================

In this exercise, you will create, deploy, and interact with your first contract.

.. topic:: Overview

    :ref:`Examine a contract <first_contract>`

    :ref:`Compile a contract <compile_contract>`

    :ref:`Deploy a contract <Deploy>`

    :ref:`Update and query the balance <update balance>`



    **Prerequisites**

        - :ref:`Set up your environment <quickstart>`.
        - Ensure your Cairo version is at least ``0.4.0`` (you can check your version by running ``cairo-compile --version``).
        - To follow this tutorial, you should have basic familiarity with writing Cairo code. For example, read the first few pages of the ":ref:`Hello, Cairo <hello_cairo>`" tutorial.



.. _first_contract:

Your first contract
-------------------

Let's start by looking at the following StarkNet contract:

.. tested-code:: cairo first_starknet_contract

    # Declare this file as a StarkNet contract and set the required
    # builtins.
    %lang starknet
    %builtins pedersen range_check

    from starkware.cairo.common.cairo_builtins import HashBuiltin
    from starkware.starknet.common.storage import Storage

    # Define a storage variable.
    @storage_var
    func balance() -> (res : felt):
    end

    # Increases the balance by the given amount.
    @external
    func increase_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(amount : felt):
        let (res) = balance.read()
        balance.write(res + amount)
        return ()
    end

    # Returns the current balance.
    @view
    func get_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}() -> (res : felt):
        let (res) = balance.read()
        return (res)
    end

File declaration:
*****************

The first line, ``%lang starknet``, declares that this file should be read as a StarkNet contract file; rather than a regular Cairo program file. Trying to compile this file with ``cairo-compile``
will result in a compilation error. StarkNet contracts should be compiled with the ``starknet-compile`` command, as we shall see below.


Add builtins:
*************

Next, we have the ``%builtins`` directive and two import statements. If you're not familiar with these types of statements, refer to the ":ref:`Hello, Cairo <hello_cairo>`" tutorial.

Define storage variables:
*************************

The first new primitive that we see in the code is ``@storage_var``.
Unlike a Cairo program, which is stateless, StarkNet contracts have a state called "the contract's storage".
Transactions invoked on such contracts may modify this state; in a way
defined by the contract.

.. _storage_var:

The ``@storage_var`` decorator declares a variable that will be kept as part of this storage.
In our case, this variable consists of a single ``felt``, called ``balance``.
To use this variable, we use the ``balance.read()`` and ``balance.write()`` functions
which are automatically created by the ``@storage_var`` decorator.
When a contract is deployed, all its storage cells are initialized to zero, i.e., all storage variables are initially zero.

Write the function/s:
*********************

StarkNet contracts have no ``main()`` function. Instead, each function may be
annotated as an external function (using the ``@external`` decorator).
External functions may be called by the users of StarkNet.
Currently, StarkNet has no authentication mechanism, so any user can invoke any external
function. If you want to restrict it, or have some authentication,
you can use the ``ecdsa`` builtin to verify a user's signature
as part of the internal implementation of the contract's function.

In our case, the contract has two external functions: ``increase_balance`` reads
the current value of balance from the storage, adds the given amount,
and writes the new value back to storage.
``get_balance`` simply reads the balance and returns its value.

.. _view_decorator:

The ``@view`` decorator is identical to the ``@external`` decorator.
The only difference is that the ``@view``method is *annotated* as a method that only queries the state rather than modifying it.
Note that in the current version, this is not enforced by the compiler.

Implicit arguments:
*******************

Consider the three implicit arguments: ``storage_ptr``, ``pedersen_ptr`` and ``range_check_ptr``:

1.  You should be familiar with ``pedersen_ptr``, computes the Pedersen hash function, and ``range_check_ptr``, which compares integers. But, it seems that the contract doesn't use any hash function or integer comparison, so why are they needed? The reason is that storage variables require these implicit arguments to compute the actual memory address of this variable. This may not be needed in simple variables such as ``balance``, but with maps (see :ref:`storage_maps`), computing the Pedersen hash is part of what ``read()`` and ``write()`` do.
2.  ``storage_ptr`` is a new primitive unique to StarkNet contracts (it doesn't exist in Cairo); it allows the code to talk with the contract's storage. This is also an implicit argument of ``read()`` and ``write()`` (this time, for more obvious reasons).

Programming without hints:
**************************

If you are familiar with programming in Cairo, you are probably familiar with :ref:`hints <hints>`. Unfortunately (or fortunately, depending on your personal opinion), using hints in StarkNet is not possible. This is due to the fact that the contract's author, the user invoking the function, and the operator running it are
likely to be different entities:

1.  The operator cannot run arbitrary python code due to security concerns.
2.  The user won't be able to verify that the operator ran the hint the contract author supplied.
3.  It is not possible to prove that nondeterministic code *failed* -- since you should either prove you executed the hint or prove that, for any hint, the code would have failed.

For efficiency, hints are still used by the standard library functions.

A function may be whitelisted by an operator if they agree to run it, i.e., when it knows that it can run its hints successfully.

NB this does not guarantee the soundness of the library function, which should be verified separately.

This means that not all the Cairo library functions can be used when writing a StarkNet contract, only those on the list. See
`here <https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/starknet/security/starknet_common.cairo>`_
for a list of the whitelisted library functions.

.. _compile_contract:

Compile the contract
--------------------

Create a file named ``contract.cairo`` and copy the contract code into it.

Run the following command to compile your contract:

.. tested-code:: bash compile_starknet

    starknet-compile contract.cairo \
        --output contract_compiled.json \
        --abi contract_abi.json

Remember, we can't compile a StarkNet contract using ``cairo-compile``, and we must use ``starknet-compile`` instead.

The contract's ABI
------------------

Let's examine the file ``contract_abi.json`` that was created during the contract's compilation:

.. tested-code:: json starknet_abi

    [
        {
            "inputs": [
                {
                    "name": "amount",
                    "type": "felt"
                }
            ],
            "name": "increase_balance",
            "outputs": [],
            "type": "function"
        },
        {
            "inputs": [],
            "name": "get_balance",
            "outputs": [
                {
                    "name": "res",
                    "type": "felt"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]

The ABI file contains a list of all the callable functions and their expected inputs.

.. _Deploy:

Deploy the contract on the StarkNet testnet
-------------------------------------------

In order to instruct the CLI to work with the StarkNet testnet, you should either pass ``--network=alpha`` on every use or set the ``STARKNET_NETWORK`` environment variable as follows:

.. tested-code:: bash starknet_env

    export STARKNET_NETWORK=alpha

**Important note**: The alpha release is an experimental release. Newer versions may require a reset of the network's state (resulting in the removal of the deployed contracts).

Run the following command to deploy your contract on the StarkNet testnet:

.. tested-code:: bash starknet_deploy

    starknet deploy --contract contract_compiled.json

The output should resemble this:

.. tested-code:: none starknet_deploy_output

    Deploy transaction was sent.
    Contract address: 0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c
    Transaction ID: 0

Note the address of your new contract. You will need this address to interact with the contract.

.. _update balance:

Interact with the contract
--------------------------

Run the following command to invoke the ``increase_balance()`` function (note that you'll have to replace ``CONTRACT_ADDRESS`` with the address you got during the contract deployment):

.. tested-code:: bash starknet_invoke

    starknet invoke \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function increase_balance \
        --inputs 1234

The result should resemble this:

.. tested-code:: none starknet_invoke_output

    Invoke transaction was sent.
    Contract address: 0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c
    Transaction ID: 1


.. _tx_status:

The following command allows you to query the transaction status based on your transaction ID (i.e., replace ``TRANSACTION_ID`` with the transaction ID printed by ``starknet invoke``):

.. tested-code:: bash starknet_tx_status

    starknet tx_status --id TRANSACTION_ID

The result should resemble this:

.. tested-code:: none starknet_tx_status_output

    {
        "block_id": 1,
        "tx_status": "PENDING"
    }

The possible statuses are:

*   ``NOT_RECEIVED``:
    The transaction has not been received yet (i.e., not written to storage).
*   ``RECEIVED``:
    The transaction was received by the operator.
*   ``PENDING``:
    The transaction passed the validation and is waiting to be sent on-chain.
*   ``REJECTED``:
    The transaction failed validation and thus was skipped.
*   ``ACCEPTED_ONCHAIN``:
    The transaction was accepted on-chain.

Query the balance
-----------------

Use the following command to query the current balance:

.. tested-code:: bash starknet_call

    starknet call \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function get_balance

The result should be:

.. tested-code:: none starknet_call_output

    1234

Note that to see the up-to-date balance, you should wait until the ``increase_balance`` transaction status is at least ``PENDING`` (that is, ``PENDING`` or ``ACCEPTED_ONCHAIN``). Otherwise, you'll see the balance before the execution of the ``increase_balance`` transaction
(that is, 0).

In the next section, we will describe other CLI functions for querying StarkNet's state.
Note that while ``deploy`` and ``invoke`` affect StarkNet's state, all other functions are read-only. In particular, using ``call`` instead of ``invoke`` on a function that *may* change the
state, such as ``increase_balance``, will return the result of the function without actually applying it to the current state, allowing the user to dry-run before committing to a state update.
