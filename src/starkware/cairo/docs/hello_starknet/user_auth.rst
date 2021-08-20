.. _user_authentication:

Adding User Authentication
==========================

.. _storage_maps:

Storage maps
------------

Suppose that instead of maintaining one global variable ``balance``,
we would like to have a balance for each user (users will be identified by
their STARK public keys).

Our first task will be to change the ``balance`` storage variable
to a map from public key (user) to balance
(instead of a single value). This can be done by simply adding an argument:

.. tested-code:: cairo balance_map

    # A map from user (public key) to a balance.
    @storage_var
    func balance(user : felt) -> (res : felt):
    end

In fact, the ``@storage_var`` decorator allows you to add multiple arguments to create
even more complicated maps.
The functions ``balance.read()`` and ``balance.write()`` will now have the following signatures:

.. code-block:: cairo

    func read{
            storage_ptr : Storage*, range_check_ptr,
            pedersen_ptr : HashBuiltin*}(
        user : felt) -> (res : felt)

    func write{
            storage_ptr : Storage*, range_check_ptr,
            pedersen_ptr : HashBuiltin*}(
        user : felt, value : felt)

Note that the default value of all the entries in the map is 0.

Signature verification
----------------------

We now have to modify ``increase_balance`` to do the following:

1.  Write to the appropriate ``balance`` entry.
2.  Verify that the user has signed on this change.

For the signature, we will use the STARK-friendly ECDSA signature,
which is natively supported in Cairo.
For technical details about this cryptographic primitive see
`STARK Curve <https://docs.starkware.co/starkex-docs/crypto/stark-curve>`_.

We will need the ``ecdsa`` builtin to verify the signature, so we will change the ``%builtins``
line to:

.. tested-code:: cairo user_auth_builtins

    %builtins pedersen range_check ecdsa

and add the following import statement:

.. tested-code:: cairo user_auth_imports

    from starkware.cairo.common.cairo_builtins import (
        HashBuiltin, SignatureBuiltin)
    from starkware.cairo.common.signature import (
        verify_ecdsa_signature)
    from starkware.cairo.common.hash import hash2
    from starkware.starknet.common.storage import Storage

Next, we will change the code of ``increase_balance()`` to:

.. tested-code:: cairo user_auth_increase_balance

    # Increases the balance of the given user by the given amount.
    @external
    func increase_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr, ecdsa_ptr : SignatureBuiltin*}(
            user : felt, amount : felt, sig_r : felt, sig_s : felt):
        # Compute the hash of the message.
        # The hash of (x, 0) is equivalent to the hash of (x).
        let (amount_hash) = hash2{hash_ptr=pedersen_ptr}(amount, 0)

        # Verify the user's signature.
        verify_ecdsa_signature(
            message=amount_hash,
            public_key=user,
            signature_r=sig_r,
            signature_s=sig_s)

        let (res) = balance.read(user=user)
        balance.write(user, res + amount)
        return ()
    end

``verify_ecdsa_signature`` behaves like an assert -- in case the signature is invalid, the function
will revert the entire transaction.

Note that we don't handle replay attacks here -- once the user signs a transaction
someone may call it multiple times. One way to prevent replay attacks is to
add a ``nonce`` argument to ``increase_balance``, change the signed message to
the Pedersen hash of the nonce and the amount and define
another storage map from the signed message to a flag (either 0 or 1)
indicating whether or not that transaction was executed by the system.
Future versions of StarkNet will handle user authentication and prevent replay attack.

Similarly, change the code of ``get_balance()``. Here we don't need to verify the signature
(since StarkNet's storage is not private anyway),
so the change is simpler:

.. tested-code:: cairo user_auth_get_balance

    # Returns the balance of the given user.
    @view
    func get_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(user : felt) -> (res : felt):
        let (res) = balance.read(user=user)
        return (res)
    end

Compile and deploy
------------------

Save the new contract file as ``user_auth.cairo``.
You can find the full Cairo file `here <../_static/user_auth.cairo>`_.

Compile and deploy the file:

.. tested-code:: bash user_auth_compile_starknet

    starknet-compile user_auth.cairo \
        --output user_auth_compiled.json \
        --abi user_auth_abi.json

    starknet deploy --contract user_auth_compiled.json

Don't forget to set ``STARKNET_NETWORK=alpha`` before running ``starknet deploy``.

Interacting with the contract
-----------------------------

First, we need to generate a pair of public and private keys.
We will use a constant private key (of course, in a real application choosing
a secure random private key is imperative).
Then, we sign a message to increase the balance by 4321.
For this, we will use the following python statements:

.. tested-code:: python user_auth_sign

    from starkware.crypto.signature.signature import (
        pedersen_hash, private_to_stark_key, sign)
    private_key = 12345
    message_hash = pedersen_hash(4321)
    public_key = private_to_stark_key(private_key)
    signature = sign(
        msg_hash=message_hash, priv_key=private_key)
    print(f'Public key: {public_key}')
    print(f'Signature: {signature}')

You should get:

.. tested-code:: python user_auth_sign_output

    Public key: 1628448741648245036800002906075225705100596136133912895015035902954123957052
    Signature: (1225578735933442828068102633747590437426782890965066746429241472187377583468, 3568809569741913715045370357918125425757114920266578211811626257903121825123)

Now, let's update the balance:

.. _user_auth_increase_balance:

.. tested-code:: bash user_auth_invoke

    starknet invoke \
        --address CONTRACT_ADDRESS \
        --abi user_auth_abi.json \
        --function increase_balance \
        --inputs \
            1628448741648245036800002906075225705100596136133912895015035902954123957052 \
            4321 \
            1225578735933442828068102633747590437426782890965066746429241472187377583468 \
            3568809569741913715045370357918125425757114920266578211811626257903121825123

You can query the transaction status:

.. tested-code:: bash user_auth_tx_status

    starknet tx_status --id TX_ID

Finally, after the transaction is executed (status ``PENDING`` or ``ACCEPTED_ONCHAIN``)
we may query the user's balance.

.. tested-code:: bash user_auth_call

    starknet call \
        --address CONTRACT_ADDRESS \
        --abi user_auth_abi.json \
        --function get_balance \
        --inputs 1628448741648245036800002906075225705100596136133912895015035902954123957052

You should get:

.. tested-code:: none user_auth_call_output

    4321

Note that if you want to use the :ref:`get_storage_at` CLI command to query the balance of a
specific user, you can no longer compute the relevant key by only supplying the name of the storage
variable. That is because the balance storage variable now requires an additional argument, namely,
the user key. Hence, you will need to supply the additional arguments when acquiring the key used in
``get_storage_at``. In our case, this translates to the following python code:

.. tested-code:: python user_auth_balance_key

    from starkware.starknet.public.abi import get_storage_var_address

    user = 1628448741648245036800002906075225705100596136133912895015035902954123957052
    user_balance_key = get_storage_var_address('balance', user)
    print(f'Storage key for user {user}:\n{user_balance_key}')

You should get:

.. tested-code:: none user_auth_balance_key_output

    Storage key for user 1628448741648245036800002906075225705100596136133912895015035902954123957052:
    142452623821144136554572927896792266630776240502820879601186867231282346767

What if we have an invalid signature?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To examine this case, we will modify the signature we obtained before by changing its second
component to 1, and then invoke ``increase_balance()`` again with this invalid signature:

.. tested-code:: bash user_auth_invalid_signature

    starknet invoke \
        --address CONTRACT_ADDRESS \
        --abi user_auth_abi.json \
        --function increase_balance \
        --inputs \
            1628448741648245036800002906075225705100596136133912895015035902954123957052 \
            4321 \
            2620967193230873397198710803425457084022525354559824107385923461037870205486 \
            1

After this, when querying the transaction status, you should get:

.. tested-code:: none user_auth_invalid_signature_output

    {
        "tx_failure_reason": {
            "code": "TRANSACTION_FAILED",
            "error_message": "Error at pc=0:71:\nSignature (2620967193230873397198710803425457084022525354559824107385923461037870205486, 1), is invalid, with respect to the public key 1628448741648245036800002906075225705100596136133912895015035902954123957052, and the message hash 4321.\nCairo traceback (most recent call last):\nUnknown location (pc=0:152)\nUnknown location (pc=0:121)",
            "tx_id": 2
        },
        "tx_status": "REJECTED"
    }


This indicates that the transaction was reverted due to an invalid signature.
Notice that the error message entry states that the error location is unknown. This is because
the StarkNet network is not aware of the source code and debug information of a contract.
To retrieve the error location and reconstruct the traceback, add the path to the relevant
compiled contract in the transaction status query, using the ``--contract`` argument. To better
display the error (and only it), add the ``--error_message`` flag as well:

.. tested-code:: bash user_auth_get_error_message

    starknet tx_status \
        --id TX_ID \
        --contract user_auth_compiled.json \
        --error_message

The output should look like:

.. tested-code:: none user_auth_get_error_message_output

    .../signature.cairo:11:5: Error at pc=0:71:
        assert ecdsa_ptr.pub_key = public_key
        ^***********************************^
    Signature (2620967193230873397198710803425457084022525354559824107385923461037870205486, 1), is invalid, with respect to the public key 1628448741648245036800002906075225705100596136133912895015035902954123957052, and the message hash 4321.
    Cairo traceback (most recent call last):
    user_auth.cairo:15:6
    func increase_balance{
         ^**************^
    user_auth.cairo:19:5
        verify_ecdsa_signature(message=amount, public_key=user, signature_r=sig_r, signature_s=sig_s)
        ^*******************************************************************************************^

.. test::

    import json
    import os
    import subprocess
    import sys
    import tempfile

    from starkware.cairo.docs.test_utils import reorganize_code

    code = reorganize_code('\n\n'.join([
        '%lang starknet',
        codes['user_auth_builtins'],
        codes['user_auth_imports'],
        'from starkware.cairo.common.cairo_builtins import HashBuiltin',
        'from starkware.starknet.common.storage import Storage',
        codes['balance_map'],
        codes['user_auth_increase_balance'],
        codes['user_auth_get_balance'],
    ]))

    user_auth_filename = os.path.join(
        os.environ['DOCS_SOURCE_DIR'], 'hello_starknet/user_auth.cairo')
    # Uncomment below to fix the file:
    # open(user_auth_filename, 'w').write(code)
    assert open(user_auth_filename).read() == code, 'Please fix user_auth.cairo.'
