The above command will produce a ``Fact`` (a hash of the outputs and the program hash). Any Ropsten
application contract or user can now query the ``isValid(Fact)`` read method of the deployed
`Fact Registry`_.

.. _Fact Registry: https://ropsten.etherscan.io/address/
    0xf0EC41069A89595ADf5f27A4a90ff2DF30D83d2E#readContract

If the result is ``True``, then that application contract or user can be confident that:

  - The Cairo program has computational integrity (validity).
  - The inputs used in that program truly produced those outputs (correctness).

An application can be built by designing and deploying an Ethereum contract that:

  - Stores the ``program_hash`` permanently to be able to recognise this unique Cairo program.
  - Accepts the outputs that come from that Cairo program.
  - Uses those values in some way.

That application contract needs to have a write method that:

  - Accepts program ``outputs``.
  - Computes the ``output_hash`` (``Keccak(outputs)``).
  - Computes the ``Fact`` (``Keccak(program_hash, outputs)``).
  - Calls the `Fact Registry`_ read method ``isValid(Fact)``.
  - Interprets the response: either ``True`` or ``False``.
  - If ``True``, applies the ``outputs`` for some application logic.

In this way, a user may interact with a Cairo program to ultimately execute a change on Ethereum
without using large amounts of expensive storage or computation.
