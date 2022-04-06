Constructors
============

A contract may need to initialize its state before it is ready for public use.
For example, one may want to designate a contract owner, that can do certain operations that other
users can't. Setting a storage variable to the owner can be done by the contract constructor.
The contract constructor is defined using the ``@constructor`` decorator and its name must
be ``constructor``.
The constructor semantics are similar to that of any other external function, except that
the constructor is guaranteed to run during the contract deployment and it cannot be invoked again
after the contract is deployed.

For example, we can define an ownable contract as follows:

.. tested-code:: cairo ownable

    %lang starknet

    from starkware.cairo.common.cairo_builtins import HashBuiltin

    # Define a storage variable for the owner address.
    @storage_var
    func owner() -> (owner_address : felt):
    end

    @constructor
    func constructor{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(owner_address : felt):
        owner.write(value=owner_address)
        return ()
    end

Save the contract as ownable.cairo, compile and deploy it.
When you deploy the contract, pass the arguments using the ``--inputs`` argument.
The number of inputs must match the signature of the constructor. Otherwise, the deploy transaction
will fail.

.. tested-code:: bash ownable_deploy

    starknet-compile ownable.cairo \
        --output ownable_compiled.json \
        --abi ownable_abi.json
    starknet deploy --contract ownable_compiled.json --inputs 123

When a contract is deployed, the contract address, contract definition hash and the constructor
calldata are included in the on-chain data.
