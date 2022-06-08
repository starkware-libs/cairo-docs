.. _deploying_from_contracts:

Deploying a contract by another contract
========================================

The deploy system call
----------------------

A contract may use the ``deploy`` system call in order to deploy
another contract. Note that the contract class of the deployed
contract must be declared before the transaction invoking the system call.
The deploy system call is defined as follows:

.. tested-code:: cairo starknet_syscall_deploy

    func deploy{syscall_ptr : felt*}(
        class_hash : felt,
        contract_address_salt : felt,
        constructor_calldata_size : felt,
        constructor_calldata : felt*,
    ) -> (contract_address : felt):
    end

As seen above, the deploy syscall expects the following arguments:

*   ``class_hash``:
    The class hash of the contract to deploy.

.. TODO(Evyatar, 01/06/2022): Add reference for classes section in the docs to here.

*   ``contract_address_salt``:
    An arbitrary value used to determine the address of the new contract.
    Using the same salt, the same ``class_hash`` and the same constructor arguments
    from the same contract will result in the same address, which means that the
    second ``deploy`` will fail.
*   ``constructor_calldata_size``:
    The size of the constructor's arguments (calldata).
    Note that this may differ from the number of arguments in the cases
    where not all the arguments are felts.
*   ``constructor_calldata``:
    A pointer to an array containing the arguments for the constructor.

The syscall returns ``contract_address``: the address of the newly deployed contract.

Consider the ownable contract in :ref:`constructors`.
The following contract is an example of using the deploy system call to
deploy new instances of the ownable contract:

.. TODO(Evyatar, 21/05/2022): Combine with Declare transaction when the documentation is ready.

.. tested-code:: cairo starknet_syscall_deploy_example

    %lang starknet

    from starkware.cairo.common.alloc import alloc
    from starkware.cairo.common.cairo_builtins import HashBuiltin
    from starkware.starknet.common.syscalls import deploy

    # Define a storage variable for the salt.
    @storage_var
    func salt() -> (value : felt):
    end

    # Define a storage variable for the class hash of ownable_contract.
    @storage_var
    func ownable_class_hash() -> (value : felt):
    end

    # An event emitted whenever deploy_ownable_contract() is called.
    @event
    func ownable_contract_deployed(contract_address : felt):
    end

    @constructor
    func constructor{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(ownable_class_hash_ : felt):
        ownable_class_hash.write(value=ownable_class_hash_)
        return ()
    end

    @external
    func deploy_ownable_contract{
        syscall_ptr : felt*,
        pedersen_ptr : HashBuiltin*,
        range_check_ptr,
    }(owner_address : felt):
        let (current_salt) = salt.read()
        let (class_hash) = ownable_class_hash.read()
        let (contract_address) = deploy(
            class_hash=class_hash,
            contract_address_salt=current_salt,
            constructor_calldata_size=1,
            constructor_calldata=cast(new (owner_address,), felt*),
        )
        salt.write(value=current_salt + 1)

        ownable_contract_deployed.emit(
            contract_address=contract_address
        )
        return ()
    end

Note that the above will work only if the desired class has been previously declared.

Using the contract
------------------

Save the new contract file as ``ownable_contract_deployer.cairo``.

Compile and declare the ownable contract as explained in :ref:`constructors`.
Note that you don't need to deploy an instance of the contract,
declaring the contract class is enough when using the ``deploy`` system call.

Set an environment variable named ``OWNABLE_CLASS_HASH`` to the class hash of
``ownable_contract.cairo``.

Compile and deploy ``ownable_contract_deployer.cairo``:

.. tested-code:: bash ownable_contract_deployer_compile_starknet

    starknet-compile ownable_contract_deployer.cairo \
        --output ownable_contract_deployer_compiled.json \
        --abi ownable_contract_deployer_abi.json

    starknet deploy --contract ownable_contract_deployer_compiled.json \
        --inputs  ${OWNABLE_CLASS_HASH}

Choose an arbitrary value for the owner address, and denote it by ``OWNER_ADDRESS``.
Now, invoke ``deploy_ownable_contract`` with ``OWNER_ADDRESS``
as the value of the ``owner_address`` argument.
Make sure the ``CONTRACT_ADDRESS`` environment variable is set to
the address you got when you deployed the contract:

.. tested-code:: bash invoke_deploy_ownable_contract

    starknet invoke \
        --address ${CONTRACT_ADDRESS} \
        --abi ownable_contract_deployer_abi.json \
        --function deploy_ownable_contract \
        --inputs OWNER_ADDRESS

This will deploy a new ``ownable_contract`` with ``OWNER_ADDRESS``
as the owner address.

The address of the contract is emitted and it is visible through the transaction
receipt as explained in :ref:`events`. The data in the events section contains the
address of the deployed contract. The events section of the receipt should look like:

.. tested-code:: none deploy_ownable_contract_receipt

    "events": [
        {
            "data": [
                "0x338027db29a197a7d5dbd49f1e15c9b6702d6a16758dda905efc751bb117153"
            ],
            "from_address": "0x7569242709918b8929078d3178ed14588348fb5459b44a41f100eb9a67dbeb6",
            "keys": [
                "0x2902eb93dff1da1a2de652946319fafe27b03601628834219f8738fc9b361d7"
            ]
        }
    ]

Use the following command to query the owner address.
Replace ``OWNABLE_CONTRACT_ADDRESS`` with the address of the deployed ``ownable_contract``:

.. tested-code:: bash get_owner_call

    starknet call \
        --address OWNABLE_CONTRACT_ADDRESS \
        --abi ownable_abi.json \
        --function get_owner

The value returned should be the ``OWNER_ADDRESS`` used before.

.. TODO(Evyatar, 01/06/2022): Link to the declare transaction documentation.

**Important note**: In the future, using the deploy syscall will be the only
way to deploy new contracts.

.. test::

    from starkware.python.utils import get_source_dir_path

    syscalls_file_path = get_source_dir_path("src/starkware/starknet/common/syscalls.cairo")
    assert codes["starknet_syscall_deploy"].replace("\nend","") in open(syscalls_file_path).read(), \
        ("Please update 'starknet_syscall_deploy' code segment to match the "
        "function definition in syscalls.cairo.")
