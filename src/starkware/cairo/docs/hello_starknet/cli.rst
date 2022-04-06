More CLI commands
=================

get_transaction
---------------

To get transaction information run the following:

.. tested-code:: bash starknet_get_transaction

    starknet get_transaction --hash TRANSACTION_HASH

The output should resemble:

.. tested-code:: none starknet_get_transaction_output

    {
        "block_hash": "0x0",
        "block_number": 0,
        "status": "ACCEPTED_ON_L2",
        "transaction": {
            "calldata": [
                "0x4d2"
            ],
            "contract_address": "0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c",
            "entry_point_selector": "0x362398bec32bc0ebb411203221a35a0301193a96f317ebe5e40be9f60d15320",
            "entry_point_type": "EXTERNAL",
            "max_fee": "0x0",
            "signature": [],
            "transaction_hash": "0x69d743891f69d758928e163eff1e3d7256752f549f134974d4aa8d26d5d7da8",
            "type": "INVOKE_FUNCTION"
        },
        "transaction_index": 1
    }

The result contains:

*   ``transaction_hash`` -- The hash of the transaction, out of all sent transactions.
*   ``status`` -- The status of the transaction. For a detailed list of supported transaction
    statuses, refer to the :ref:`tx_status <tx_status>` usage example.
*   ``transaction`` -- The transaction data.

It may also include each of the following optional fields (according to the transaction's status):

*   ``block_hash`` -- The hash of the block containing the transaction.
*   ``block_number`` -- The sequence number of the block containing the transaction.
*   ``transaction_index`` -- The index of the transaction within the block containing it.
*   ``transaction_failure_reason`` -- The reason for the transaction failure.

get_transaction_receipt
-----------------------

Transaction receipt contains execution information, such as L1<->L2 interaction and consumed
resources, in addition to its block information, similar to get_transaction.
To get the transaction's receipt, run the following:

.. tested-code:: bash starknet_get_transaction_receipt

    starknet get_transaction_receipt --hash TRANSACTION_HASH

The output should resemble:

.. tested-code:: none starknet_get_transaction_receipt_output

    {
        "actual_fee": "0x0",
        "block_hash": "0x0",
        "block_number": 0,
        "events": [],
        "execution_resources": {
            "builtin_instance_counter": {
                "bitwise_builtin": 0,
                "ec_op_builtin": 0,
                "ecdsa_builtin": 0,
                "output_builtin": 0,
                "pedersen_builtin": 2,
                "range_check_builtin": 8
            },
            "n_memory_holes": 22,
            "n_steps": 168
        },
        "l2_to_l1_messages": [
            {
                "from_address": "0x7dacca7a41e893630664a61f4d8ec05550ca1a212849c62417cb3ecf4bad863",
                "payload": [
                    "0x0",
                    "0xbc614e",
                    "0x3e8"
                ],
                "to_address": "0x9E4c14403d7d9A8A782044E86a93CAE09D7B2ac9"
            }
        ],
        "status": "ACCEPTED_ON_L2",
        "transaction_hash": "0x7797c6673a1a0aeebbcb1c726702e263e5138123124ddef7edd85cd925b11ec",
        "transaction_index": 2
    }

The result contains (in addition to get_transaction fields):

*   ``l2_to_l1_messages`` -- Messages sent from L2 to L1.
*   ``l1_to_l2_consumed_message`` -- The consumed message, in case the transaction was sent from L1.
*   ``execution_resources`` -- Resources consumed by the transaction execution.

get_transaction_trace
---------------------

Transaction trace contains execution information in a nested structure of calls; every call,
starting from the external transaction, contains a list of inner calls, ordered chronologically.
For each such call, the trace holds the following: caller/callee addresses,
selector, calldata along with execution information such as its return value,
emitted events, and sent messages.

To get the transaction's trace, run the following:

.. tested-code:: bash starknet_get_transaction_trace

    starknet get_transaction_trace --hash TRANSACTION_HASH

The output should resemble:

.. tested-code:: none starknet_get_transaction_trace_output

    {
        "function_invocation": {
            "calldata": [
                "0xbc614e",
                "0x3e8"
            ],
            "caller_address": "0x0",
            "code_address": "0x3ae7fee16103cd5d9c09a8160cdd9ebd9a75c530bbafa53d9b7c920542ca1f3",
            "contract_address": "0x3ae7fee16103cd5d9c09a8160cdd9ebd9a75c530bbafa53d9b7c920542ca1f3",
            "entry_point_type": "EXTERNAL",
            "events": [],
            "execution_resources": {
                "builtin_instance_counter": {
                    "bitwise_builtin": 0,
                    "ec_op_builtin": 0,
                    "ecdsa_builtin": 0,
                    "output_builtin": 0,
                    "pedersen_builtin": 2,
                    "range_check_builtin": 8
                },
                "n_memory_holes": 22,
                "n_steps": 168
            },
            "internal_calls": [],
            "messages": [
                {
                    "order": 0,
                    "payload": [
                        "0x0",
                        "0xbc614e",
                        "0x3e8"
                    ],
                    "to_address": "0xd62F98664F8f7A1aec2F7cB602aF1f2354A881D2"
                }
            ],
            "result": [],
            "selector": "0x15511cc3694f64379908437d6d64458dc76d02482052bfb8a5b33a72c054c77"
        },
        "signature": []
    }

estimate_fee
------------

You can estimate the fee of a given transaction before invoking it.
The following command is similar to ``starknet call``, but it returns the estimated fee associated
with the transaction. You can read more about the fee mechanism
`here <https://starknet.io/documentation/fee-mechanism/>`__. The result is presented in WEI
and ETH, as shown below.

Note that ``estimate_fee`` does not change the state of the contracts. For example, the following
code will not affect the balance stored in ``BALANCE_CONTRACT``.

To estimate the fee of a given transaction run the following:

.. tested-code:: bash starknet_estimate_fee

    starknet estimate_fee \
        --address CONTRACT_ADDRESS \
        --abi contract_abi.json \
        --function increase_balance \
        --inputs 1234

The output should resemble:

.. tested-code:: none starknet_estimate_fee_output

    The estimated fee is: 259600000000000 WEI (0.000260 ETH).

get_code
--------

Once the ``deploy`` transaction is accepted on-chain, you will be able to see the code of the
contract you have just deployed. The output consists of a list of bytecodes, rather than
the source code. This is because the StarkNet network gets the contract after compilation.

To get the contract at a specific address, run the following command:

.. tested-code:: bash starknet_get_code

    starknet get_code --contract_address CONTRACT_ADDRESS

The output should resemble:

.. tested-code:: none starknet_get_code_output

    {
        "abi": [
            {
                "inputs": [
                    {
                        "name": "amount",
                        "type": "felt"
                    }
                ],
                "name": "increase_balance",
                "outputs": [],
                "type": "function"
            },

            ...

            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x208b7fff7fff7ffe"
        ]
    }

get_full_contract
-----------------

To get the full contract definition of a contract at a specific address, run the following command:

.. tested-code:: bash starknet_get_full_contract

    starknet get_full_contract --contract_address CONTRACT_ADDRESS

The output should resemble:

.. tested-code:: none starknet_get_full_contract_output

    {
        "abi": [
            {
                "inputs": [
                    {
                        "name": "amount",
                        "type": "felt"
                    }
                ],
                "name": "increase_balance",
                "outputs": [],
                "type": "function"
            },

            ...

        }
    }

get_block
---------

Instead of querying a specific contract or transaction, you may want to query an entire block and
examine the transactions contained within it.
To do this, run the following:

.. tested-code:: bash starknet_get_block

    starknet get_block --number BLOCK_NUMBER

The output should resemble:

.. tested-code:: none starknet_get_block_output

    {
        "block_hash": "0x39a53f921b51af73e95ecf13ffe1542da069f680531e8a36b2f6b656e45a162",
        "block_number": 0,
        "parent_block_hash": "0x0",
        "state_root": "079354de0075c5c1f2a6af40c7dd70a92dc93c68b54ecc327b61c8426fea177c",
        "status": "ACCEPTED_ON_L2",
        "timestamp": 105,
        "transaction_receipts": [
            {
                "actual_fee": "0x0",
                "events": [],
                "execution_resources": {
                    "builtin_instance_counter": {},
                    "n_memory_holes": 0,
                    "n_steps": 0
                },
                "l2_to_l1_messages": [],
                "transaction_hash": "0x50f392748f303a37f0a9053b7295d51231bee3e0a9dbf42bcb1c8392e4d8503",
                "transaction_index": 0
            },
            {
                "actual_fee": "0x0",
                "events": [],
                "execution_resources": {
                    "builtin_instance_counter": {
                        "bitwise_builtin": 0,
                        "ec_op_builtin": 0,
                        "ecdsa_builtin": 0,
                        "output_builtin": 0,
                        "pedersen_builtin": 0,
                        "range_check_builtin": 0
                    },
                    "n_memory_holes": 0,
                    "n_steps": 65
                },
                "l2_to_l1_messages": [],
                "transaction_hash": "0x1ba395964b6d4308b14a78a8f6f59dbc0c753ad966e5d3e1e3118ca29e10841",
                "transaction_index": 1
            }
        ],
        "transactions": [
            {
                "class_hash": "0x711941b11a8236b8cca42b664e19342ac7300abb1dc44957763cb65877c2708",
                "constructor_calldata": [],
                "contract_address": "0x05a4d278dceae5ff055796f1f59a646f72628730b7d72acb5483062cb1ce82dd",
                "contract_address_salt": "0x0",
                "transaction_hash": "0x602e4b4e9e046d2692af3702fe013fef996df040af335223e7526c9c4fe6fb",
                "type": "DEPLOY"
            },
            {
                "calldata": [
                    "0x4d2"
                ],
                "contract_address": "0x05a4d278dceae5ff055796f1f59a646f72628730b7d72acb5483062cb1ce82dd",
                "entry_point_selector": "0x362398bec32bc0ebb411203221a35a0301193a96f317ebe5e40be9f60d15320",
                "entry_point_type": "EXTERNAL",
                "max_fee": "0x0",
                "signature": [],
                "transaction_hash": "0x142ca10924ad813764aa8f7ac7c298721708bf531d12d6e5fc4bda3cf9c7904",
                "type": "INVOKE_FUNCTION"
            }
        ]
    }

.. TODO(Adi, 15/08/2021): Below it should be last *accepted* block.

The result contains:

*   ``block_hash`` -- The block hash, a unique identifier of the block.
*   ``parent_block_hash`` -- the block hash of the parent block.
*   ``block_number`` -- The sequence number of the block, which is the number of
    blocks prior to this block.
*   ``state_root`` -- The root of a commitment tree representing the StarkNet's state after the given
    block.
*   ``status`` -- The status of the block (for example, ``ACCEPTED_ON_L2``, which means that the block
    was created but has not been accepted on-chain yet).
*   ``timestamp`` -- A timestamp representing the time this block was created.
*   ``transaction_receipts`` -- Information about the transaction status and the corresponding
    L1<->L2 interaction, for every transaction included in the block.
*   ``transactions`` -- A mapping of the transactions included in the block, according to their
    transaction hashes. Note that these are the same hashes used in the ``transaction_receipts`` mapping.

To query the last block, simply remove the ``--number`` argument.
To query a block by hash, use ``--hash`` instead. Note that at most one of these arguments can be
given.

get_state_update
----------------

You can use the following command to get the state changes in a specific
block (for example, what storage cells have changed):

.. tested-code:: bash starknet_get_state_update

    starknet get_state_update --block_number BLOCK_NUMBER

The output should resemble:

.. tested-code:: none starknet_get_state_update_output

    {
        "block_hash": "0x1cbab9fde46b7e8d1a913148226e1f236b38fea96cbdaef65c44523e66a6a58",
        "new_root": "057d148812170fae78ffa5c219b72ee487b714678884c3b2d409716c5520ef46",
        "old_root": "0000000000000000000000000000000000000000000000000000000000000000",
        "state_diff": {
            "deployed_contracts": [
                {
                    "address": "0x7c5b47040c4e1d8d7937e7daf5bafba2db1f8a28fdb72cd53dd0c857a7dd2d9",
                    "contract_hash": "03b9181402fccc351a4fa4084f606c1e7c7d30cc5c58eb62fc12d1decc6b3004"
                }
            ],
            "storage_diffs": {
                "0x7c5b47040c4e1d8d7937e7daf5bafba2db1f8a28fdb72cd53dd0c857a7dd2d9": [
                    {
                        "key": "0x206f38f7e4f15e87567361213c28f235cccdaa1d7fd34c9db1dfe9489c6a091",
                        "value": "0x4d2"
                    }
                ]
            }
        }
    }

The result contains:

*   ``block_hash`` -- The block hash, a unique identifier of the block.
*   ``new_root`` -- The root of a commitment tree representing the StarkNet's state after the given
    block.
*   ``old_root`` -- The root of a commitment tree representing the StarkNet's state before the given
    block.
*   ``state_diff`` -- The changes in the state applied in this block, given as a mapping of
    addresses to the new values and/or new contracts.

To query the last block, simply remove the ``--number`` argument.
To query a block by hash, use ``--block_hash`` instead.
Note that at most one of these arguments can be given.

.. _get_storage_at:

get_storage_at
--------------

Other than querying the contract's code, you may also want to query the contract's storage at a
specific key. To do so, you first need to understand which key is of interest to you.
As you saw before, StarkNet introduces a new primitive, which is
:ref:`storage variables <storage_var>`. Each storage variable is mapped to a storage key (a field
element).
To compute this key, run the following python code:

.. tested-code:: python get_variable_key

    from starkware.starknet.public.abi import get_storage_var_address

    balance_key = get_storage_var_address('balance')
    print(f'Balance key: {balance_key}')

You should get:

.. tested-code:: python get_variable_key_output

    Balance key: 916907772491729262376534102982219947830828984996257231353398618781993312401

Now, you can query the balance using:

.. tested-code:: bash starknet_get_storage_at

    starknet get_storage_at \
        --contract_address CONTRACT_ADDRESS \
        --key 916907772491729262376534102982219947830828984996257231353398618781993312401

Using the same contract we have used so far, you should get:

.. tested-code:: none starknet_get_storage_at_output

    0x4d2

Note that this is the same result obtained by the call to ``get_balance``.

Later on, at the :ref:`user authentication <user_authentication>` section, you will see :ref:`a
generalization of storage variables <storage_maps>`, which allow, for example, a balance
variable for each user. This will require minor adjustments to the code above, which we will review
in the relevant section.

.. TODO(Adi, 15/08/2021): At the end of the second paragraph below, change to last *accepted* block.

Block-specific queries
**********************

Some of the aforementioned CLI functions have an additional argument, ``--block_hash``, which
applies the given query to a specific block.
For example, you may want to query the balance variable at some specific point in time.

To find out whether a CLI function can be executed as a block-specific query, simply use the
``--help`` argument to see if ``--block_hash`` is part of the optional arguments for that function.
In case you do not use the ``--block_hash`` argument, the query will be applied to the last block.
