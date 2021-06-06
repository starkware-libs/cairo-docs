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

.. tested-code:: cairo library_builtins_hashbuiltin

    from starkware.cairo.common.cairo_builtins import HashBuiltin
    from starkware.cairo.common.hash import hash2

    func foo{hash_ptr : HashBuiltin*}() -> (hash):
        # The hash_ptr is a pointer to a HashBuiltin struct.
        # It is passed implicitly to hash2().
        let (my_hash) = hash2(5,13)
        return (hash=my_hash)
    end

``SignatureBuiltin``
********************

Returns a representation of a ``SignatureBuiltin`` struct, specifying the signature builtin memory
structure.

-   ``pub_key``, .
-   ``message``, .

.. tested-code:: cairo library_builtins_signaturebuiltin

    from starkware.cairo.common.cairo_builtins import SignatureBuiltin

    alloc_locals
    local new_signature : SignatureBuiltin

``CheckpointsBuiltin``
**********************

Returns a representation of a ``CheckpointsBuiltin`` struct, specifying
the checkpoint builtin memory structure.

-   ``required_pc``, .
-   ``required_fp``, .

.. tested-code:: cairo library_builtins_checkpointsbuiltin

    from starkware.cairo.common.cairo_builtins import CheckpointsBuiltin

    alloc_locals
    local new_checkpoint : CheckpointsBuiltin
