.. proofedDate 2021/11/23

.. comment null

.. _user_authentication:


Add User Authentication
=======================

.. topic:: Overview

    :ref:`Handle multiple Users <storage_maps>`

    :ref:`Verify signatures <verify signature>`

    :ref:`Compile and deploy <Compile and deploy>`

    :ref:`Update and query the balance <update a balance>`

    :ref:`Handle invalid signatures <invalid signature>`

.. _storage_maps:

Storage maps
------------

Suppose that, instead of maintaining one global variable ``balance``,
we would like to have a balance for each User (as identified by
their STARK public key).

Our first task is to change the ``balance`` storage variable
to a map from public key (User) to balance
(instead of a single value). This can be achieved by adding an argument:

.. tested-code:: cairo balance_map

    # A map from User (public key) to a balance.
    @storage_var
    func balance(user : felt) -> (res : felt):
    end

In fact, the ``@storage_var`` decorator allows you to add multiple arguments to create even more complicated maps.
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

.. _verify signature:

Signature verification
----------------------

We now have to modify ``increase_balance`` to do the following:

1.  Write to the appropriate ``balance`` entry.
2.  Verify that the User has signed on this change.

For the signature, we will use the STARK-friendly ECDSA signature, which is natively supported in Cairo.
For technical details about this cryptographic primitive, see
`STARK Curve <https://docs.starkware.co/starkex-docs/crypto/stark-curve>`_.

We will need the ``ecdsa`` builtin to verify the signature, so we will change the ``%builtins`` line to:

.. tested-code:: cairo user_auth_builtins

    %builtins pedersen range_check ecdsa

and add the following import statement:

.. tested-code:: cairo user_auth_imports

    from starkware.cairo.common.cairo_builtins import (
        HashBuiltin, SignatureBuiltin)
    from starkware.cairo.common.hash import hash2
    from starkware.cairo.common.signature import (
        verify_ecdsa_signature)
    from starkware.starknet.common.storage import Storage

Next, we will change the code of ``increase_balance()`` to:

.. tested-code:: cairo user_auth_increase_balance

    # Increases the balance of the given User by the given amount.
    @external
    func increase_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr, ecdsa_ptr : SignatureBuiltin*}(
            user : felt, amount : felt, sig_r : felt, sig_s : felt):
        # Compute the hash of the message.
        # The hash of (x, 0) is equivalent to the hash of (x).
        let (amount_hash) = hash2{hash_ptr=pedersen_ptr}(amount, 0)

        # Verify the User's signature.
        verify_ecdsa_signature(
            message=amount_hash,
            public_key=user,
            signature_r=sig_r,
            signature_s=sig_s)

        let (res) = balance.read(user=user)
        balance.write(user, res + amount)
        return ()
    end

``verify_ecdsa_signature`` behaves like an assert -- in the case that the signature is invalid, the function will revert the entire transaction.

.. topic:: Note

    Note that we don't handle replay attacks here. In a replay, once the User signs a transaction, someone may call it multiple times.
    One way to prevent replay attacks is to add a ``nonce`` argument to ``increase_balance``, change the signed message to
    the Pedersen hash of the nonce and the amount, and define
    another storage map from the signed message to a flag (either 0 or 1) -- indicating whether or not that transaction was executed by the system.
    Future versions of StarkNet will handle User authentication and prevent replay attacks.


Similar to the code change for ``increase_balance()`` , we adjust ``get_balance()`` to handle the balance mapping. Here we don't need to verify the signature (since StarkNet's storage is not private anyway), so the change is simpler:

.. tested-code:: cairo user_auth_get_balance

    # Returns the balance of the given User.
    @view
    func get_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            range_check_ptr}(user : felt) -> (res : felt):
        let (res) = balance.read(user=user)
        return (res)
    end

.. _Compile and deploy:

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

.. topic:: Important

    Don't forget to set ``STARKNET_NETWORK=alpha`` before running ``starknet deploy``.

.. _update a balance:

Interact with the contract
--------------------------

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

Finally, after the transaction is executed (status ``PENDING`` or ``ACCEPTED_ONCHAIN``), we may query the User's balance.

.. tested-code:: bash user_auth_call

    starknet call \
        --address CONTRACT_ADDRESS \
        --abi user_auth_abi.json \
        --function get_balance \
        --inputs 1628448741648245036800002906075225705100596136133912895015035902954123957052

You should get:

.. tested-code:: none user_auth_call_output

    4321

Note that if you want to use the :ref:`get_storage_at` CLI command to query the balance of a specific User, you can no longer compute the relevant key by only supplying the name of the storage variable. That is because the balance storage variable now requires an additional argument, namely,
the User key. Hence, you will need to supply the additional arguments when acquiring the key used in ``get_storage_at``. In our case, this translates to the following python code:

.. tested-code:: python user_auth_balance_key

    from starkware.starknet.public.abi import get_storage_var_address

    user = 1628448741648245036800002906075225705100596136133912895015035902954123957052
    user_balance_key = get_storage_var_address('balance', user)
    print(f'Storage key for user {user}:\n{user_balance_key}')

You should get:

.. tested-code:: none user_auth_balance_key_output

    Storage key for user 1628448741648245036800002906075225705100596136133912895015035902954123957052:
    142452623821144136554572927896792266630776240502820879601186867231282346767

.. _invalid signature:

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
            1225578735933442828068102633747590437426782890965066746429241472187377583468 \
            1

After this, when querying the transaction status, you should get:

.. tested-code:: none user_auth_invalid_signature_output

    {
        "tx_failure_reason": {
            "code": "TRANSACTION_FAILED",
            "error_message": "Error at pc=0:71:\nSignature (1225578735933442828068102633747590437426782890965066746429241472187377583468, 1), is invalid, with respect to the public key 1628448741648245036800002906075225705100596136133912895015035902954123957052, and the message hash 2145928028330445730928899764978337236302436665109337681432022680924515407233.\nCairo traceback (most recent call last):\nUnknown location (pc=0:155)\nUnknown location (pc=0:127)",
            "tx_id": 2
        },
        "tx_status": "REJECTED"
    }


This indicates that the transaction was reverted due to an invalid signature. Notice that the error message entry states that the error location is unknown. This is because the StarkNet network is not aware of the contract's source code and debug information.
To retrieve the error location and reconstruct the traceback, add the path to the relevant compiled contract in the transaction status query, using the ``--contract`` argument. To better display the error (and only it), add the ``--error_message`` flag as well:

.. tested-code:: bash user_auth_get_error_message

    starknet tx_status \
        --id TX_ID \
        --contract user_auth_compiled.json \
        --error_message

The output should resemble this:

.. tested-code:: none user_auth_get_error_message_output

    .../signature.cairo:11:5: Error at pc=0:71:
        assert ecdsa_ptr.pub_key = public_key
        ^***********************************^
    Signature (1225578735933442828068102633747590437426782890965066746429241472187377583468, 1), is invalid, with respect to the public key 1628448741648245036800002906075225705100596136133912895015035902954123957052, and the message hash 2145928028330445730928899764978337236302436665109337681432022680924515407233.
    Cairo traceback (most recent call last):
    user_auth.cairo:16:6
    func increase_balance{
         ^**************^
    user_auth.cairo:24:5
        verify_ecdsa_signature(
        ^*********************^

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

