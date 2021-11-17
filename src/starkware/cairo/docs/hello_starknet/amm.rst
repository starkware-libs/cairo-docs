.. proofedDate 2021/11/23

.. _Uniswap: https://docs.uniswap.org/protocol/V2/concepts/protocol-overview/how-uniswap-works

.. _library: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo

.. _code: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/starknet/apps/amm_sample/amm_sample.cairo

.. _amm_starknet:

A simple Automated Market Maker (AMM)
=====================================

.. topic:: Overview

    **TL;DR**

    - Get: scalability & security for AMM
    - By: keeping the AMM state in a contract's storage and maintaining it with the contract's functions

    **Contents**

    :ref:`Implement AMM <Implement AMM>`

    :ref:`Understand the AMM state <The AMM state>`

    :ref:`Swap tokens <Swap tokens>`

    :ref:`Initialize the AMM <Initialize the AMM>`

    :ref:`Explore examples <Explore examples>`

    **Prerequisites**

    In order to understand the basics of Automated Market Making (AMM), you may:

        - refer to the Uniswap_ docs, or
        - check the short description in our previous :ref:`AMM tutorial <amm_cairo>`.

This tutorial reviews the code of a simple AMM written as a StarkNet contract; it highlights
specific implementation details. The contract is deployable (and is actually deployed
-- `go check it out <https://amm-demo.starknet.starkware.co>`_)
to the StarkNet Planets Alpha release. It will be seamlessly deployable and compatible with
future StarkNet releases.

We start by describing the scope of the contract functionality and follow with a dive into the
implementation.
Finally, we demonstrate how to invoke the demo contract's functionality on the StarkNet Planets
Alpha environment with concrete examples.

Before we begin, you can review the full contract code `here
<https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/starknet/
apps/amm_sample/amm_sample.cairo>`_.

.. _Implement AMM:

AMM implementation in StarkNet Planets Alpha
--------------------------------------------

For those who read the :ref:`previous tutorial <amm_cairo>` -- comparing the code written there to
the contract code in this tutorial can be an illuminating exercise that highlights the power of
StarkNet.

In this sample contract, we will:

    * limit our functionality to exactly one Pool to be managed by the contract

    * implement a straightforward swap functionality (in both directions) using a simple curve, i.e., the constant product formula (:math:`x \cdot y = k`)

    * refer to the tokens managed by the AMM as token A and token B, which represent any type of fungible token


For simplicity, some functionality related to interaction with ERC20 contracts will be mocked
inside the AMM, i.e., minting tokens in an ERC20 contract are mocked in this sample contract.
In practice, this logic would be implemented inside an ERC20 contract.

The important point from this example is how StarkNet enables the developer of the Application to
focus on specifying the verifiable business logic and constraints;
while enjoying massive scalability -- without compromising security. In other words, only the
invocable functions and the relevant storage variables used to maintain the state of the
Application need to be specified by the developer.


.. _The AMM state:

The AMM state
--------------

Next, we dive into the implementation. We will start by reviewing how we maintain the state of the
AMM.

We require the following fields in order to maintain the state:


1.  the Pool balance -- how much liquidity is available in the Pool per token.
2.  the account balances -- how many tokens of each type are kept in each account

.. topic:: Note

    As explained above, item 2 is only needed for this release and will be replaced with regular
    ERC-20 interactions in the future.

In StarkNet, the programmatic model for storage is a simple key/value store.
We can define a :ref:`storage variable <storage_var>`, so reading and writing from/to
storage is just a matter of calling ``read`` and ``write`` on that variable.

The Pool balance is defined as a mapping between the token type (predefined constants) and the
balance available in the Pool for that token type.:

.. tested-code:: cairo sn_amm_pool_balance

    @storage_var
    func pool_balance(token_type : felt) -> (balance : felt):
    end

The account balance is defined as a mapping between the account Id and token type, to the balance
available in that account, for the given token type.

.. tested-code:: cairo sn_amm_account_balance

    @storage_var
    func account_balance(account_id : felt, token_type : felt) -> (
            balance : felt):
    end


Next, we write a function that *modifies* the balance of a given token type in a given account:

.. tested-code:: cairo sn_amm_modify_account

    func modify_account_balance{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_type : felt, amount : felt):
        let (current_balance) = account_balance.read(
            account_id, token_type)
        tempvar new_balance = current_balance + amount
        assert_nn_le(new_balance, BALANCE_UPPER_BOUND - 1)
        account_balance.write(
            account_id=account_id,
            token_type=token_type,
            value=new_balance)
        return ()
    end

The logic is fairly straightforward:

    1. retrieve the existing account balance
    2. calculate the new balance
    3. assert it is not negative and doesn't exceed the upper bound
    4. write it to the account balance storage variable

Observe that this flow covers cases where we subtract an amount from, or add an amount to, the
balance.

.. topic:: Note

    As mentioned, we assume that the reader is familiar with Cairo syntax.
    For those who are not, briefly, the relevant concepts are:

    The usage of :ref:`implicit arguments <implicit_arguments>` passed to the
    `modify_account_balance` function inside the curly brackets. Specifically, the arguments
    necessary for the assertion and storage operations. Wherever such functionality is used,
    we will pass these implicit arguments.

    The assert functions used here are imported from Cairo's common math library_. In this case,
    ``assert_nn_le`` asserts that the first argument is non-negative and is less than or equal to
    the second argument (as *per* **3** above).

To allow a User to read the balance of an account, we define the following:

:ref:`view function <view_decorator>`:

.. tested-code:: cairo sn_amm_get_account

    @view
    func get_account_token_balance{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_type : felt) -> (
            balance : felt):
        return account_balance.read(account_id, token_type)
    end

Similarly, for the Pool balance:

.. tested-code:: cairo sn_amm_get_set_account

    func set_pool_token_balance{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_type : felt, balance : felt):
        assert_nn_le(balance, BALANCE_UPPER_BOUND - 1)
        pool_balance.write(token_type, balance)
        return ()
    end

    @view
    func get_pool_token_balance{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_type : felt) -> (balance : felt):
        return pool_balance.read(token_type)
    end

.. _Swap tokens:

Swap tokens
-----------

Next, the primary function of the contract -- swapping tokens.

.. tested-code:: cairo sn_amm_swap

    func swap{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_from : felt,
            amount_from : felt) -> (amount_to : felt):
        # Verify that token_from is either TOKEN_TYPE_A or TOKEN_TYPE_B.
        assert (token_from - TOKEN_TYPE_A) * (token_from - TOKEN_TYPE_B) = 0

        # Check requested amount_from is valid.
        assert_nn_le(amount_from, BALANCE_UPPER_BOUND - 1)

        # Check User has enough funds.
        let (account_from_balance) = get_account_token_balance(
            account_id=account_id, token_type=token_from)
        assert_le(amount_from, account_from_balance)

        # Execute the actual swap.
        let (token_to) = get_opposite_token(token_type=token_from)
        let (amount_to) = do_swap(
            account_id=account_id,
            token_from=token_from,
            token_to=token_to,
            amount_from=amount_from)

        return (amount_to=amount_to)
    end

``swap`` receives as inputs the account id, the token type, and the amount of the token to be
swapped. The function starts by verifying the validity of the inputs:

    *   the token type is a valid token by asserting that it is equal to one of the Pool's token types

    *   the swap amount requested is valid, i.e., it does not exceed the upper bound, and the account has enough funds to swap

If all checks pass, we proceed to execute the swap:

.. tested-code:: cairo sn_amm_do_swap

    func do_swap{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_from : felt, token_to : felt,
            amount_from : felt) -> (amount_to : felt):
        alloc_locals

        # Get pool balance.
        let (local amm_from_balance) = get_pool_token_balance(
            token_type=token_from)
        let (local amm_to_balance) = get_pool_token_balance(
            token_type=token_to)

        # Calculate swap amount.
        let (local amount_to, _) = unsigned_div_rem(
            amm_to_balance * amount_from,
            amm_from_balance + amount_from)

        # Update token_from balances.
        modify_account_balance(
            account_id=account_id,
            token_type=token_from,
            amount=-amount_from)
        set_pool_token_balance(
            token_type=token_from,
            balance=amm_from_balance + amount_from)

        # Update token_to balances.
        modify_account_balance(
            account_id=account_id,
            token_type=token_to,
            amount=amount_to)
        set_pool_token_balance(
            token_type=token_to, balance=amm_to_balance - amount_to)
        return (amount_to=amount_to)
    end

The logic of the swapping itself is fairly straightforward:

    1. retrieve the amount of tokens available in the Pool, per token type
    2. calculate the amount of tokens of the opposite type to be received by the Pool
    3. update the account balances for both tokens, as well as the Pool's balances

Most of this implementation invokes functions we described earlier (``get_pool_token_balance``,
``modify_account_balance``, and``set_pool_token_balance``).


Note that the calculation of the amount to be swapped essentially implements the AMM constant
product formula:

:math:`\text{amount_to} =
\frac{\text{amm_to_balance} \cdot \text{amount_from}}
{\text{amm_from_balance} + \text{amount_from}}`

We use Cairo's common math library, specifically ``unsigned_div_rem`` (unsigned division with
remainder), to calculate the amount of tokens to be received.

.. _Initialize the AMM:

Initialize the AMM
-------------------

As we don't have contract interaction and liquidity providers in this version, we will now define
how to initialize the AMM: both the liquidity Pool itself and some account balances.

.. tested-code:: cairo sn_amm_init_amm

    @external
    func init_pool{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_a : felt, token_b : felt):
        assert_nn_le(token_a, POOL_UPPER_BOUND - 1)
        assert_nn_le(token_b, POOL_UPPER_BOUND - 1)

        set_pool_token_balance(token_type=TOKEN_TYPE_A, bal=token_a)
        set_pool_token_balance(token_type=TOKEN_TYPE_B, bal=token_b)

        return ()
    end

Initializing the Pool is a simple function that accepts two balances for the tokens (A and B), and
sets them using the ``set_pool_token_balance`` function we defined above:
The ``POOL_UPPER_BOUND`` is a constant defined to prevent overflows.

Having this function defined, we proceed to add demo tokens to an account:

.. tested-code:: cairo sn_amm_add_tokens

    @external
    func add_demo_token{
            syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_a_amount : felt,
            token_b_amount : felt):
        # Make sure the account's balance is much smaller than Pool init balance.
        assert_nn_le(token_a_amount, ACCOUNT_BALANCE_BOUND - 1)
        assert_nn_le(token_b_amount, ACCOUNT_BALANCE_BOUND - 1)

        modify_account_balance(
            account_id=account_id,
            token_type=TOKEN_TYPE_A,
            amount=token_a_amount)
        modify_account_balance(
            account_id=account_id,
            token_type=TOKEN_TYPE_B,
            amount=token_b_amount)

        return ()
    end

Note that here we add another business constraint (for demo purposes) that the account is capped at
some number calculated as a ratio from the Pool cap. Specifically, ``ACCOUNT_BALANCE_BOUND`` is
defined as ``POOL_UPPER_BOUND`` divided by 1000, so the cap for an account is 1/1000 that of a Pool.
All constants are defined at the top of the contract file.

.. _Explore examples:

Interaction examples
--------------------

.. topic:: Prerequisites

    * the reader is familiar with the StarkNet CLI. If this is not the case, we recommend you review this :ref:`section <starknet_intro>`

    * the ``STARKNET_NETWORK`` environment variable is set as alpha:

    .. tested-code:: bash amm_starknet_env

        export STARKNET_NETWORK=alpha

    * for this section, you need to have the contract code.


.. test::

    assert codes['starknet_env'] == codes['amm_starknet_env']

We can now explore a few examples which demonstrate how to interact with the contract using the
StarkNet CLI tool. An instance of this contract is deployed and initialized at address ``0x05``.


To use the StarkNet CLI, start by generating the ABI of the contract:

.. tested-code:: bash amm_sample_compile

    starknet-compile amm_sample.cairo \
        --output amm_sample_compiled.json \
        --abi amm_sample_abi.json

First, you can query the Pool's balance using:

.. tested-code:: bash sn_amm_call_pool_balance

    starknet call \
        --address ${AMM_ADDRESS} \
        --abi amm_sample_abi.json \
        --function get_pool_token_balance \
        --inputs 1

In response, you should get the Pool's balance of token A.

Now let's add some tokens to our account's balance. Choose your favorite ``ACCOUNT_ID``, it should
be a 251-bit integer value:

.. tested-code:: bash account_id

    export ACCOUNT_ID="<favorite 251-bit integer>"


.. tested-code:: bash sn_amm_invoke_add_tokens

    starknet invoke \
        --address ${AMM_ADDRESS} \
        --abi amm_sample_abi.json \
        --function add_demo_token \
        --inputs ${ACCOUNT_ID} 1000 1000

Now that we have some tokens, we can use the AMM and swap 500 units of token A in exchange for some
units of token B (the exact number depends on the current balance of the Pool).

.. tested-code:: bash sn_amm_invoke_swap

    starknet invoke \
        --address ${AMM_ADDRESS} \
        --abi amm_sample_abi.json \
        --function swap \
        --inputs ${ACCOUNT_ID} 1 500

You can now query the account's balance of token B after the swap:

.. tested-code:: bash sn_amm_call_account_balance

    starknet call \
        --address ${AMM_ADDRESS} \
        --abi amm_sample_abi.json \
        --function get_account_token_balance \
        --inputs ${ACCOUNT_ID} 2

Note that the change will only take effect after the ``swap`` transaction's status
is either ``PENDING`` or ``ACCEPTED_ONCHAIN``.
