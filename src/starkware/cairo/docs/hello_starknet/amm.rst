.. _amm_starknet:

A simple Automated Market Maker (AMM)
=====================================

In this tutorial, we'll review the code of a simple AMM, written as a StarkNet contract,
highlighting specific implementation details. The contract is deployable (and is actually deployed
-- `go check it out <https://amm-demo.starknet.starkware.co>`_)
to the StarkNet Planets Alpha release, and will be seamlessly deployable
and compatible with future StarkNet releases.

We'll start by describing the scope of the contract functionality,
and after that will dive into the implementation.
Finally, we'll show how to invoke the demo contract's functionality on the StarkNet Planets Alpha
environment with a few concrete examples.

Before we begin, you can review the full contract code `here
<https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/starknet/
apps/amm_sample/amm_sample.cairo>`_

AMM implementation in StarkNet Planets Alpha
--------------------------------------------

In order to understand the basics of automated market making, you may refer
to the `Uniswap docs <https://uniswap.org/docs/v2/protocol-overview/how-uniswap-works/>`_, or
check the short description in our previous :ref:`AMM tutorial <amm_cairo>`.
For those who read the previous tutorial -- comparing the code written there to the contract code
in this tutorial can be a fun exercise that highlights the power of StarkNet.

In this sample contract we'll limit our functionality to exactly one pool to be managed by the
contract. We will implement a straightforward swap functionality (in both directions),
using a simple curve; i.e. the constant product formula (:math:`x \cdot y = k`). We will refer to
the tokens managed by the AMM as token A and token B, which may play the role of any type of
fungible tokens.

Also, since StarkNet Planets Alpha does not support contract interaction,
some aspects that ideally would've been implemented in other contracts, e.g. minting tokens in an
ERC20 contract, are mocked in this sample contract. This functionality is not inherent to AMM
functionality.

What's important to learn from this example is how StarkNet allows the developer of the
application to focus on specifying his verifiable business logic and constraints,
all while enjoying massive scalability without compromising security. In other words,
only the invocable functions and the relevant storage variables used to maintain the state of the
application need to be specified by the developer.

The AMM state
--------------

Let's dive into the implementation. We'll start by reviewing how we maintain the state of the AMM.

We require two dedicated fields in order to maintain the state:

1.  The pool balance -- how much liquidity is available in the pool, per token.
2.  The account balances -- how many tokens of each type are kept in each account.
    As explained above, this is only needed for this release,
    and will be replaced with regular ERC-20 interactions in the future.

In StarkNet, the programmatic model for storage is a simple key/value store.
We can define a :ref:`storage variable <storage_var>`, so reading and writing from/to
storage is simply a matter of calling ``read`` and ``write`` on that variable.

For the pool balance we define:

.. tested-code:: cairo sn_amm_pool_balance

    @storage_var
    func pool_balance(token_type : felt) -> (balance : felt):
    end

The pool balance is defined as a mapping between the token type (predefined constants) and the
balance available in the pool for that token type.

For the account balances we define:

.. tested-code:: cairo sn_amm_account_balance

    @storage_var
    func account_balance(account_id : felt, token_type : felt) -> (
            balance : felt):
    end

The account balance is defined as a mapping between a the account id and token type,
to the balance available in that account, for the given token type.

We write a function that allows us to *modify* the balance of a given token type in a given account:

.. tested-code:: cairo sn_amm_modify_account

    func modify_account_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
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

* Retrieve the existing account balance.
* Calculate the new balance.
* Assert it is not negative and doesn't exceed the upper bound.
* Write it to the account balance storage variable.

Note that this also covers cases where we subtract an amount from the balance.

As mentioned before, we assume that the reader is familiar with Cairo syntax.
For those who are not, we briefly mention the relevant concepts.

First, we observe the usage of :ref:`implicit arguments <implicit_arguments>` passed to this
function inside the curly brackets. Specifically, the arguments necessary for the assertion and
storage operations. Wherever such functionality is used, we'll pass these implicit arguments.

Next, the assert functions used here are imported from Cairo's `common math library
<https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo>`_
. In this case, ``assert_nn_le`` asserts that the first
argument is non-negative and is less than or equal to the second argument.

To allow a user to read the balance of an account, we define the following
:ref:`view function <view_decorator>`:

.. tested-code:: cairo sn_amm_get_account

    @view
    func get_account_token_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_type : felt) -> (
            balance : felt):
        return account_balance.read(account_id, token_type)
    end

Similarly, for the pool balance:

.. tested-code:: cairo sn_amm_get_set_account

    func set_pool_token_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_type : felt, balance : felt):
        assert_nn_le(balance, BALANCE_UPPER_BOUND - 1)
        pool_balance.write(token_type, balance)
        return ()
    end

    @view
    func get_pool_token_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_type : felt) -> (balance : felt):
        return pool_balance.read(token_type)
    end

Swapping tokens
----------------

We now proceed to the primary functionality of the contract -- swapping tokens.

.. tested-code:: cairo sn_amm_swap

    func swap{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_from : felt,
            amount_from : felt) -> (amount_to : felt):
        # Verify that token_from is either TOKEN_TYPE_A or TOKEN_TYPE_B.
        assert (token_from - TOKEN_TYPE_A) * (token_from - TOKEN_TYPE_B) = 0

        # Check requested amount_from is valid.
        assert_nn_le(amount_from, BALANCE_UPPER_BOUND - 1)

        # Check user has enough funds.
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

``swap`` receives as inputs the account id, the token type and an amount of the token to be swapped.
The function starts by verifying the validity of the inputs:

*   The token type is a valid token, by asserting that it is equal to one of the pool's
    token types.
*   The amount requested to be swapped is valid -- it does not exceed the upper bound, and the
    account has enough funds to swap.

If all checks pass, we proceed to execute the swap.

.. tested-code:: cairo sn_amm_do_swap

    func do_swap{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
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

1. Retrieve the amount of tokens available in the pool, per token type.
2. Calculate the amount of tokens of the opposite type to be received by the pool.
3. Update the account balances for both tokens, as well as the pool's balances.

Most of this implementation invokes functions we described earlier (``get_pool_token_balance``,
``modify_account_balance``, ``set_pool_token_balance``). Note that the calculation of the
amount to be swapped essentially implements the AMM constant product formula:

:math:`\text{amount_to} =
\frac{\text{amm_to_balance} \cdot \text{amount_from}}
{\text{amm_from_balance} + \text{amount_from}}`

We use Cairo's common math library, specifically ``unsigned_div_rem``
(unsigned division with remainder) to calculate the amount of tokens to be received.

Initializing the AMM
---------------------

As we don't have contract interaction and liquidity providers in this version, we will now define
how to initialize the AMM -- both the liquidity pool itself and some account balances.

.. tested-code:: cairo sn_amm_init_amm

    @external
    func init_pool{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(token_a : felt, token_b : felt):
        assert_nn_le(token_a, POOL_UPPER_BOUND - 1)
        assert_nn_le(token_b, POOL_UPPER_BOUND - 1)

        set_pool_token_balance(token_type=TOKEN_TYPE_A, bal=token_a)
        set_pool_token_balance(token_type=TOKEN_TYPE_B, bal=token_b)

        return ()
    end

Initializing the pool is a simple function that accepts two balances for the tokens (A,B),
and sets them using the ``set_pool_token_balance`` function we defined above:
The ``POOL_UPPER_BOUND`` is a constant defined to prevent overflows.

Having this function defined, we proceed to add demo tokens to an account:

.. tested-code:: cairo sn_amm_add_tokens

    @external
    func add_demo_token{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(
            account_id : felt, token_a_amount : felt,
            token_b_amount : felt):
        # Make sure the account's balance is much smaller then pool init balance.
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

Note that here we add another business constraint (for demo purposes) that the account is capped
at some number calculated as a ratio from the pool cap. Specifically, ``ACCOUNT_BALANCE_BOUND``
is defined as ``POOL_UPPER_BOUND`` divided by 1000, so the cap for an account is 1/1000 that of a
pool.
All constants are defined at the top of the contract file.

Interaction examples
--------------------

We can now explore a few examples which demonstrate contract interaction using the StarkNet CLI
tool. An instance of this contract is deployed and initialized at address ``0x05``.

We assume the reader is familiar with the StarkNet CLI. If this is not the case, we recommend you
review this :ref:`section <starknet_intro>`.
Also we assume the ``STARKNET_NETWORK`` environment variable is set as follows:

.. tested-code:: bash amm_starknet_env

    export STARKNET_NETWORK=alpha

.. test::

    assert codes['starknet_env'] == codes['amm_starknet_env']

For this section you need to have the contract code, you can find it `here
<https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/starknet/
apps/amm_sample/amm_sample.cairo>`_.

To use the StarkNet CLI, start by generating the ABI of the contract:

.. tested-code:: bash amm_sample_compile

    starknet-compile amm_sample.cairo \
        --output amm_sample_compiled.json \
        --abi amm_sample_abi.json

First, you can query the pool's balance using:

.. tested-code:: bash sn_amm_call_pool_balance

    starknet call \
        --address 5 \
        --abi amm_sample_abi.json \
        --function get_pool_token_balance \
        --inputs 1

In response, you should get the pool's balance of token 1.

Now let's add some tokens to our account's balance. Choose your favorite ``ACCOUNT_ID``, it should
be a 251-bit integer value:

.. tested-code:: bash sn_amm_invoke_add_tokens

    starknet invoke \
        --address 5 \
        --abi amm_sample_abi.json \
        --function add_demo_token \
        --inputs ACCOUNT_ID 1000 1000

Now that we have some tokens, we can use the AMM and swap 500 units of token 1 in exchange for
some units of token 2 (the exact number depends on the current balance of the pool).

.. tested-code:: bash sn_amm_invoke_swap

    starknet invoke \
        --address 5 \
        --abi amm_sample_abi.json \
        --function swap \
        --inputs ACCOUNT_ID 1 500

You can now query the account's balance of token 2 after the swap:

.. tested-code:: bash sn_amm_call_account_balance

    starknet call \
        --address 5 \
        --abi amm_sample_abi.json \
        --function get_account_token_balance \
        --inputs ACCOUNT_ID 2

Note that the change will only take effect after the ``swap`` transaction's status
is either ``PENDING`` or ``ACCEPTED_ONCHAIN``.
