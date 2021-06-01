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

    func read{storage_ptr : Storage*, pedersen_ptr : HashBuiltin*}(
        user : felt) -> (res : felt)

    func write{storage_ptr : Storage*, pedersen_ptr : HashBuiltin*}(
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

We will need the ``ecdsa`` builtin to verify the signature, so change the ``%builtins`` line to:

.. tested-code:: cairo user_auth_builtins

    %builtins pedersen ecdsa

and add the following import statement:

.. tested-code:: cairo user_auth_imports

    from starkware.cairo.common.cairo_builtins import (
        SignatureBuiltin)
    from starkware.cairo.common.signature import (
        verify_ecdsa_signature)

Next, change the code of ``increase_balance()`` to:

.. tested-code:: cairo user_auth_increase_balance

    # Increases the balance of the given user by the given amount.
    @external
    func increase_balance{
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*,
            ecdsa_ptr : SignatureBuiltin*}(
            user : felt, amount : felt, sig_r : felt, sig_s : felt):
        # Verify the user's signature.
        verify_ecdsa_signature(
            message=amount,
            public_key=user,
            signature_r=sig_r,
            signature_s=sig_s)

        let (res) = balance.read(user=user)
        balance.write(user, res + amount)
        return ()
    end

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
            storage_ptr : Storage*, pedersen_ptr : HashBuiltin*}(
            user : felt) -> (res : felt):
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
        --output=user_auth_compiled.json

    starknet deploy --program user_auth_compiled.json

.. test::

    import json
    import os
    import subprocess
    import sys
    import tempfile

    from starkware.cairo.docs.test_utils import reorganize_code

    PRIME = 2**251 + 17 * 2**192 + 1

    code = reorganize_code('\n\n'.join([
        '%lang starknet',
        codes['user_auth_builtins'],
        codes['user_auth_imports'],
        'from starkware.cairo.common.cairo_builtins import HashBuiltin',
        'from starkware.starknet.core.storage.storage import Storage',
        codes['balance_map'],
        codes['user_auth_increase_balance'],
        codes['user_auth_get_balance'],
    ]))

    user_auth_filename = os.path.join(
        os.environ['DOCS_SOURCE_DIR'], 'hello_starknet/user_auth.cairo')
    # Uncomment below to fix the file:
    # open(user_auth_filename, 'w').write(code)
    assert open(user_auth_filename).read() == code, 'Please fix user_auth.cairo.'

