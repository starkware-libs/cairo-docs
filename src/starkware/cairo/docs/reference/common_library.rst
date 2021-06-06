``cairo_builtins``
------------------

This section contains builtin structs from the ``cairo_builtins`` library.

``HashBuiltin``
***************

Returns a representation of a ``HashBuiltin struct``, specifying the hash builtin memory structure.

.. tested-code:: cairo library_builtins_hashbuiltin

    from starkware.cairo.common.cairo_builtins import HashBuiltin

    alloc_locals
    local new_hash : HashBuiltin

``SignatureBuiltin``
********************

Returns a representation of a ``SignatureBuiltin struct``, specifying the signature builtin memory
structure.

.. tested-code:: cairo library_builtins_signaturebuiltin

    from starkware.cairo.common.cairo_builtins import SignatureBuiltin

    alloc_locals
    local new_signature : SignatureBuiltin

``CheckpointsBuiltin``
**********************

Returns a representation of a ``CheckpointsBuiltin struct``, specifying
the checkpoint builtin memory structure.

.. tested-code:: cairo library_builtins_checkpointsbuiltin

    from starkware.cairo.common.cairo_builtins import CheckpointsBuiltin

    alloc_locals
    local new_checkpoint : CheckpointsBuiltin
