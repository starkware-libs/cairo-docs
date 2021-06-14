The above command will produce a ``Fact`` (a hash of the outputs and the program hash). Any Ropsten
application contract or user can now query the ``isValid(Fact)`` read method of the deployed
`Fact Registry`_.

.. _Fact Registry: https://ropsten.etherscan.io/address/
    0xf0EC41069A89595ADf5f27A4a90ff2DF30D83d2E#readContract

If the result is ``True``, then that application contract or user can be confident that:

-   The Cairo program has computational integrity (validity).
-   The inputs used in that program truly produced those outputs (correctness).

An application can be built by designing and deploying an Ethereum contract that:

-   Stores the ``program_hash`` permanently to be able to recognise this unique Cairo program.
-   Accepts the outputs that come from that Cairo program.
-   Uses those values in some way.

**Application Design**

That application contract needs to have a method that performs particular steps.
The steps and some corresponding Solidity examples are outlined below for a function
called ``updateState()``, which:

#.  Accepts, as an argument, the Cairo program outputs.

    - ``function updateState(uint256[] memory programOutput) public {}``.

#.  Computes the output hash.

    - ``bytes32 outputHash = keccak256(abi.encodePacked(programOutput));``.

#.  Computes the ``fact``, which is a keccak hash of the Pedersen hash of the program
    and the program outputs. The program hash is permanent and can be retrieved from
    contract storage.

    - ``bytes32 fact = keccak256(abi.encodePacked(cairoProgramHash_, outputHash));``.

#.  Calls the `Fact Registry`_ read method ``isValid(fact)`` to determine if the proof
    should be accepted. The address of the verifier is permament and can be
    retrieved from contract storage.

    - ``require(cairoVerifier_.isValid(fact), "MISSING_CAIRO_PROOF");``.

#.  Updates the application state, accessing the program outputs by index,
    according to the specific application.

    - ``applicationState_ = programOutput[1]``.

In this way, a user may interact with a Cairo program to ultimately execute a change on Ethereum
without using large amounts of expensive storage or computation.

**Application Deployment**

A solidity contract ``CairoApplication.sol`` can be deployed to use the fact in the
``FactRegistry`` contract for its logic. That contract may have a function ``updateState()``
which can be called by passing outputs from ``MyProgram.cairo`` as arguments. The function
call would be a transaction that updates the state of the application to reflect the
state changes that the Cairo program created.

**Application Use**

A user, or agent on behalf of a user, can interact with the application by following the steps:

1. Create an ``inputs.json`` file with custom values.
2. Obtain a copy of ``MyProgram.cairo``.
3. Install Cairo and compile the program.
4. Submit the program to SHARP for proving.
5. Call ``updateState()`` function in the ``CairoApplication`` contract.

These steps can be abstracted away from the user experience with the use of an interface and
server backend.