More CLI commands
=================

get_code
--------

Once the ``deploy`` transaction is accepted on-chain, you will be able to see the code of the
contract you have just deployed. The output consists of a list of bytecodes, rather than
the source code. That is because the StarkNet network gets the contract after compilation.

To get the contract at a specific address, run the following command:

.. tested-code:: bash starknet_get_code

    starknet get_code --contract_address CONTRACT_ADDRESS

The output should look like:

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

            290341444919459839,
            1,
            4611826758063194110,
            5193354042767540224,
            5193354042767540224,
            5189976364521848832,
            1,
            5193354042767540224,
            2345108766317314046
        ]
    }

.. TODO(Adi, 15/06/2021): Explain about the --block_id argument in both get_code and get_storage_at.

get_block
---------

Instead of querying a specific contract, you may want to query an entire block and examine the
transactions contained within it.
To do this, run the following:

.. tested-code:: bash starknet_get_block

    starknet get_block --id BLOCK_ID

The output should look like:

.. tested-code:: none starknet_get_block_output

    {
        "block_id": 0,
        "previous_block_id": -1,
        "sequence_number": 0,
        "state_root": "069513ec3fe63e082c841ce3545a1059c54a513295fbd256ba04453953b94a4a",
        "status": "PENDING",
        "timestamp": 105,
        "txs": {
            "0": {
                "contract_address": "0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c",
                "type": "DEPLOY"
            }
        }
    }


.. TODO(Adi, 15/06/2021): Below it should be last *accepted* block.

The result contains:

*   The block id, a unique identifier of the block, along with the id of the previous block.
*   The sequence number of the block, which is the number of blocks prior to this block.
*   The root of a Merkle tree representing the StarkNet's state after the given block.
*   The status of the block (for example, PENDING, which means that the block was created but has
    not been accepted on-chain yet).
*   A timestamp representing the time this block was created.
*   The list of transactions included in the block.

To query the last block, simply remove the ``--id`` argument.


.. TODO(Adi, 07/06/2021): Mention abi.py in get_storage_at.
