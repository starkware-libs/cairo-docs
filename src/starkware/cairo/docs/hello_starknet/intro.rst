.. _starknet_intro:

Writing StarkNet contracts
==========================

In order to follow this tutorial you should have basic familiarity with writing
Cairo code. For example, you can read the first few pages of the
":ref:`Hello, Cairo <hello_cairo>`" tutorial.
You should also :ref:`set up your environment <quickstart>` and make sure your
installed Cairo version is at least ``$[VERSION]``
(you can check your version by running ``cairo-compile --version``).

.. _first_contract:

Your first contract
-------------------

Let's start by looking at the following StarkNet contract:

.. tested-code:: cairo first_starknet_contract

    # Declare this file as a StarkNet contract.
    %lang starknet

    from starkware.cairo.common.cairo_builtins import HashBuiltin

    # Define a storage variable.
    @storage_var
    func balance() -> (res : felt):
    end

    # Increases the balance by the given amount.
    @external
    func increase_balance{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(amount : felt):
        let (res) = balance.read()
        balance.write(res + amount)
        return ()
    end

    # Returns the current balance.
    @view
    func get_balance{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }() -> (res : felt):
        let (res) = balance.read()
        return (res=res)
    end

The first line, ``%lang starknet`` declares that this file should be read as a StarkNet contract
file, rather than a regular Cairo program file. Trying to compile this file with ``cairo-compile``
will result in a compilation error. Compiling StarkNet contracts should be done with the
``starknet-compile`` command as we shall see below.

Next, we have two import statements. If you're not familiar with
this type of statement, refer to the ":ref:`Hello, Cairo <hello_cairo>`" tutorial.
Note that you don't need to explicitly use the ``%builtins`` directive in StarkNet contracts.

The first new primitive that we see in the code is ``@storage_var``.
Unlike a Cairo program, which is stateless, StarkNet contracts have a state,
called "the contract's storage".
Transactions invoked on such contracts may modify this state, in a way
defined by the contract.

.. _storage_var:

The ``@storage_var`` decorator declares a variable which will be kept as part of this storage.
In our case, this variable consists of a single ``felt``, called ``balance``.
To use this variable, we will use the ``balance.read()`` and ``balance.write()`` functions
which are automatically created by the ``@storage_var`` decorator.
When a contract is deployed, all its storage cells are initialized to zero.
In particular, all storage variables are initially zero.

StarkNet contracts have no ``main()`` function. Instead, each function may be
annotated as an external function (using the ``@external`` decorator).
External functions may be called by the users of StarkNet, and by other contracts
(see :ref:`calling_contracts`).

In our case, the contract has two external functions: ``increase_balance`` reads
the current value of balance from the storage, adds the given amount to it
and writes the new value back to storage.
``get_balance`` simply reads the balance and returns its value.

.. _view_decorator:

The ``@view`` decorator is identical to the ``@external`` decorator.
The only difference is that the method is *annotated* as a method that only queries the state
rather than modifying it.
Note that in the current version this is not enforced by the compiler.

Consider the three implicit arguments:
``syscall_ptr``, ``pedersen_ptr`` and ``range_check_ptr``:

1.  You should be familiar with ``pedersen_ptr``, which allows to compute the Pedersen
    hash function, and ``range_check_ptr``, which allows to compare integers.
    But it seems that the contract doesn't use any hash function or integer comparison,
    so why are they needed?
    The reason is that storage variables require these implicit arguments in order to compute
    the actual memory address of this variable. This may not be needed in simple variables
    such as ``balance``, but with maps (see :ref:`storage_maps`) computing the Pedersen hash
    is part of what ``read()`` and ``write()`` do.
2.  ``syscall_ptr`` is a new primitive, unique to StarkNet contracts
    (it doesn't exist in Cairo). ``syscall_ptr`` allows the code to invoke system calls.
    It is also implicit arguments of ``read()`` and ``write()``
    (this time, because storage access is done using system calls).

Programming without hints
*************************

If you are familiar with programming in Cairo,
you are probably familiar with :ref:`hints <hints>`.
Unfortunately (or fortunately, depending on your personal opinion), using hints
in StarkNet is not possible. This is due to the fact that
the contract's author, the user invoking the function and the operator running it are
likely to be different entities:

1.  The operator cannot run arbitrary python code due to security concerns.
2.  The user won't be able to verify that the operator ran the hint the contract author supplied.
3.  It is not possible to prove that nondeterministic code *failed*, since you should
    either prove you executed the hint or prove that for any hint the code would've failed.

For efficiency, hints are still used by the standard library functions, through a mechanism
of whitelisting (a function is whitelisted by an operator if it agrees to run it,
when it knows that it can run its hints successfully. It doesn't have to do with the question
of the soundness of the library function, which should be verified separately).
This means that not all the Cairo library functions can be used when writing
a StarkNet contract. See
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

As mentioned above, we can't compile StarkNet contract using ``cairo-compile``
and we need to use ``starknet-compile`` instead.

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

.. _declare_contract:

Declare the contract on the StarkNet testnet
--------------------------------------------

In order to instruct the CLI to work with the StarkNet testnet you should either
pass ``--network=alpha-goerli`` on every use, or set the ``STARKNET_NETWORK`` environment variable
as follows:

.. tested-code:: bash starknet_env

    export STARKNET_NETWORK=alpha-goerli

Unlike Ethereum, StarkNet distinguishes between a contract class and a contract instance.
A contract class represents the code of a contract (but with no state), while a contract instance
represents a specific instance of the class, with its own state.

Run the following command to declare your contract class on the StarkNet testnet:

.. tested-code:: bash starknet_declare

    starknet declare --contract contract_compiled.json

The output should look like:

.. tested-code:: none starknet_declare_output

    Declare transaction was sent.
    Contract class hash: $[INTRO_CONTRACT_CLASS_HASH]
    Transaction hash: 0x762e166dd3326b2e263eb5bcfdccd225dc88e067fdf7c92cf8ce5e4ea01f9f1

You can see here the class hash of your new contract. You'll need this class hash in order to
deploy an instance of the contract using the :ref:`deploy system call <deploying_from_contracts>`.

**Note**: You are not required to declare a contract before deploying it when using the ``deploy``
command. The ``deploy`` command also declares the contract.

Deploy the contract on the StarkNet testnet
-------------------------------------------

**Important note**: The alpha release is an experimental release. Newer versions may
require a reset of the network's state (resulting in the removal of the deployed contracts).

Run the following command to deploy your contract on the StarkNet testnet:

.. tested-code:: bash starknet_deploy

    starknet deploy --contract contract_compiled.json

The output should look like:

.. tested-code:: none starknet_deploy_output

    Deploy transaction was sent.
    Contract address: $[INTRO_CONTRACT_ADDRESS]
    Transaction hash: 0x125e4bc5251af8ee2664ea0d1495b36c593f25f78f1a78f637a3f7aafa9e22

You can see here the address of your new contract. You'll need this address to interact with
the contract.

Set the following environment variable:

.. tested-code:: bash intro_contract_address

    # The deployment address of the previous contract.
    export CONTRACT_ADDRESS="<address of the previous contract>"

Interact with the contract
--------------------------

Run the following command to invoke the ``increase_balance()``:

.. tested-code:: bash starknet_invoke

    starknet invoke \
        --address ${CONTRACT_ADDRESS} \
        --abi contract_abi.json \
        --function increase_balance \
        --inputs 1234

The result should look like:

.. tested-code:: none starknet_invoke_output

    Invoke transaction was sent.
    Contract address: $[INTRO_CONTRACT_ADDRESS]
    Transaction hash: 0x69d743891f69d758928e163eff1e3d7256752f549f134974d4aa8d26d5d7da8

**Note**: Due to the use of fees in StarkNet, every interaction with a contract through
a function invocation must be done using an account. To set up an account, see :ref:`account_setup`.

.. _tx_status:

The following command allows you to query the transaction status based on the transaction hash
that you got (here you'll have to replace ``TRANSACTION_HASH`` with the transaction hash printed by
``starknet invoke``):

.. tested-code:: bash starknet_tx_status

    starknet tx_status --hash TRANSACTION_HASH

The result should look like:

.. tested-code:: none starknet_tx_status_output

    {
        "block_hash": "0x0",
        "tx_status": "ACCEPTED_ON_L2"
    }

The possible statuses are:

*   ``NOT_RECEIVED``:
    The transaction has not been received yet (i.e., not written to storage).
*   ``RECEIVED``:
    The transaction was received by the sequencer.
*   ``PENDING``:
    The transaction passed the validation and entered the pending block.
*   ``REJECTED``:
    The transaction failed validation and thus was skipped.
*   ``ACCEPTED_ON_L2``:
    The transaction passed the validation and entered an actual created block.
*   ``ACCEPTED_ON_L1``:
    The transaction was accepted on-chain.

Query the balance
-----------------

Use the following command to query the current balance:

.. tested-code:: bash starknet_call

    starknet call \
        --address ${CONTRACT_ADDRESS} \
        --abi contract_abi.json \
        --function get_balance

The result should be:

.. tested-code:: none starknet_call_output

    1234

Note that to see the up-to-date balance you should wait until the ``increase_balance``
transaction status is at least ``ACCEPTED_ON_L2`` (that is, ``ACCEPTED_ON_L2`` or ``ACCEPTED_ON_L1``).
Otherwise, you'll see the balance before the execution of the ``increase_balance`` transaction
(that is, 0).

In the next section we will describe other CLI functions for querying StarkNet's state.
Note that while ``deploy`` and ``invoke`` affect StarkNet's state, all other functions are
read-only. In particular, using ``call`` instead of ``invoke`` on a function that may change the
state, such as ``increase_balance``, will return the result of the function without actually
applying it to the current state, allowing the user to dry-run before committing to a state update.
