.. proofedDate 2021/11/23

.. comments .. _change_query_context link not working on Ariel's build think it is fine on mine (Harries), just dropping to bottom of page, yes?

.. suggestedEdit1 ?I did not see this in last reviewable sweep?{wip "transaction_id": 1, looks like the actualy property and its value, so why do we SHOUT it in the bash command as TRANSACTION_ID ? Is the capitalization genuine?} > If Not Consider a less shouty form [output is transaction_id, seems nice!]

More CLI commands
=================


.. topic:: Overview

    :ref:`Get transaction information <get_transaction>`

    :ref:`Get contract code <get_code>`

    :ref:`Query a block <get_block>`

    :ref:`Get storage by key <get_storage_at>`

    :ref:`Change query context <change_query_context>`

    And remember, you can always ask for ``--help``.

.. _get_transaction:

get_transaction
---------------

To get transaction information, run the following:

.. tested-code:: bash starknet_get_transaction

    starknet get_transaction --id TRANSACTION_ID

The output should resemble this:

.. tested-code:: none starknet_get_transaction_output

    {
        "block_id": 1,
        "block_number": 1,
        "status": "PENDING",
        "transaction": {
            "calldata": [
                "1234"
            ],
            "contract_address": "0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c",
            "entry_point_selector": "0x362398bec32bc0ebb411203221a35a0301193a96f317ebe5e40be9f60d15320",
            "entry_point_type": "EXTERNAL",
            "type": "INVOKE_FUNCTION"
        },
        "transaction_id": 1,
        "transaction_index": 0
    }


The result contains:

*   ``transaction_id``: The Id of the transaction, out of all sent transactions.
*   ``status``: The status of the transaction. For a detailed list of supported transaction
    statuses, refer to the :ref:`tx_status <tx_status>` usage example.
*   ``transaction``: The transaction data.

It may also include each of the following optional fields (according to the transaction's status):

*   ``block_id``: The Id of the block containing the transaction.
*   ``block_number``: The sequence number of the block containing the transaction.
*   ``transaction_index``: The index of the transaction within its containing block.
*   ``transaction_failure_reason``: The reason for the transaction's failure.


.. _get_code:

get_code
--------

Once the ``deploy`` transaction is accepted on-chain, you will be able to see the code of the
contract you have just deployed. The output consists of a list of bytecodes rather than the source
code. This is because the StarkNet network gets the contract after compilation.

To get the contract at a specific address, run the following command:

.. tested-code:: bash starknet_get_code

    starknet get_code --contract_address CONTRACT_ADDRESS

The output should resemble this:

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

            5189976364521848832,
            1,
            5193354034177605632,
            2345108766317314046
        ]
    }

.. _get_block:

get_block
---------

Instead of querying a specific contract or transaction, you may want to query an entire block and
examine the transactions contained within it.
To do this, run the following:

.. tested-code:: bash starknet_get_block

    starknet get_block --id BLOCK_ID

The output should resemble this:

.. tested-code:: none starknet_get_block_output

    {
        "block_id": 0,
        "previous_block_id": -1,
        "sequence_number": 0,
        "state_root": "069513ec3fe63e082c841ce3545a1059c54a513295fbd256ba04453953b94a4a",
        "status": "PENDING",
        "timestamp": 105,
        "transaction_receipts": {},
        "transactions": {
            "0": {
                "contract_address": "0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c",
                "type": "DEPLOY"
            }
        }
    }


.. TODO(Adi, 15/08/2021): Below it should be last *accepted* block.

The result contains:

*   ``block_id``: The block Id, a unique identifier of the block.
*   ``previous_block_id``: The block Id of the previous block.
*   ``sequence_number``: The block's sequence number, i.e., the number of blocks prior to this block.
*   ``state_root``: The root of a commitment tree representing the StarkNet's state after the given
block.
*   ``status``: The status of the block (for example, ``PENDING`` -- i.e., the block was created but
has not been accepted on-chain yet).
*   ``timestamp``: A timestamp representing the time this block was created.
*   ``transaction_receipts``: Information about the transaction status and the corresponding L1<->L2
interaction for every transaction included in the block.
*   ``transactions``: A mapping of the transactions included in the block, according to their
transaction Ids. Note that these are the same Ids used in the ``transaction_receipts`` mapping.

To query the last block, remove the ``--id`` argument.

.. _get_storage_at:

get_storage_at
--------------

Besides querying the contract's code, you may also want to query the contract's storage at a
specific key. To do so, you first need to understand which key is of interest to you.
As you saw before, StarkNet introduces a new primitive:
:ref:`storage variables <storage_var>`. Each storage variable is mapped to a storage key
(a field element).
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

    1234

Note that this is the same result obtained by the call to ``get_balance``.


Later on, at the :ref:`User authentication <user_authentication>` section, you will see :ref:`a
generalization of storage variables <storage_maps>`, which allow, for example, a balance variable
for each User. This will require minor adjustments to the code above, which we will review in the
relevant section.


.. _change_query_context:

Block-specific queries
----------------------

Some of these CLI functions accept an additional argument, ``--block_id``, which applies the given
query to a specific block.
This assists, for example, when you want to query the balance variable at a specific point in time.

To determine whether a CLI function can be executed as a block-specific query, use the ``--help``
argument to see if ``--block_id`` is an optional argument for that function.
Without the ``--block_id`` argument, the query is applied to the last accepted block.
