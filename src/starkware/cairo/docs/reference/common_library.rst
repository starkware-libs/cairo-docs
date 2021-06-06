``cairo_builtins``
------------------

This section contains builtin structs from the ``cairo_builtins`` library.

``HashBuiltin``
***************

Returns a representation of a ``HashBuiltin`` struct, specifying the hash builtin memory structure.
This struct is used by functions from the common library to represent the elements to be
hashed. For example, the ``hash2()`` function accepts an implicit argument of type
``HashBuiltin*``, which is used internally to enable hashes to be tracked within a Cairo program.

The struct has the following members:

-   ``x``, a ``felt``.
-   ``y``, a ``felt``.
-   ``result``, a ``felt`` representing the hash of ``x`` and ``y``.

In the example below, ``foo()`` accepts two numbers and returns their Pedersen
hash ``hash(a, b)``.

.. tested-code:: cairo library_builtins_hashbuiltin

    from starkware.cairo.common.cairo_builtins import HashBuiltin
    from starkware.cairo.common.hash import hash2

    func foo{hash_ptr : HashBuiltin*}(
            a : felt, b : felt) -> (hash):
        # hash_ptr is a pointer to a HashBuiltin struct.
        # It is passed implicitly to hash2().
        let (my_hash) = hash2(a, b)
        return (hash=my_hash)
    end

``SignatureBuiltin``
********************

Returns a representation of a ``SignatureBuiltin`` struct, specifying the signature
builtin memory structure. This struct is used by functions from the common library to represent
the elements to be hashed. For example, the ``verify_ecdsa_signature()`` function accepts an
implicit argument of type ``SignatureBulitin*``, which is used internally to enable
signatures to be tracked within a Cairo program.

-   ``pub_key``, a ``felt`` representing an ECDSA public key.
-   ``message``, a ``felt`` representing a message signed by the ``pub_Key``.

.. tested-code:: cairo library_builtins_signaturebuiltin

    from starkware.cairo.common.cairo_builtins import (
        SignatureBuiltin)
    from starkware.cairo.common.signature import (
        verify_ecdsa_signature)

    func foo{ecdsa_ptr : SignatureBuiltin*}(
            msg, pubkey, r, s):
        # ecdsa_ptr is a pointer to a SignatureBuiltin struct.
        # It is passed implicitly to the function below.
        verify_ecdsa_signature(
            message=msg,
            public_key=vote_info_ptr.pub_key,
            signature_r=vote_info_ptr.r,
            signature_s=vote_info_ptr.s)
        return ()
    end

``CheckpointsBuiltin``
**********************

Returns a representation of a ``CheckpointsBuiltin`` struct, specifying
the checkpoint builtin memory structure. This struct is used where a checkpoint
is required. For example, a function, ``foo()`` may require access to the
``checkpoints_ptr`` which would have the type ``CheckpointsBuiltin*``.

-   ``required_pc``, a ``felt`` representing ``pc``.
-   ``required_fp``, a ``felt`` representing ``fp``.

.. tested-code:: cairo library_builtins_checkpointsbuiltin

    from starkware.cairo.common.cairo_builtins import (
        CheckpointsBuiltin)

    func foo{checkpoints_ptr : CheckpointsBuiltin*}():
        # Code requiring a checkpoint here.
        return ()
    end
