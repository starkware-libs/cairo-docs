# testing

Testing utilities for Starknet contracts.
This module provides functions for testing Starknet contracts. The functions
allow manipulation of blockchain state and storage variables during tests, as well as
inspection of emitted events and messages.
Note: The functions in this module can only be used with the `cairo-test` testing framework.
If you are using Starknet Foundry, refer to its
documentation.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[testing](./core-starknet-testing.md)


[Free functions](./core-starknet-testing-free_functions.md)
 ---
| | |
|:---|:---|
| [set_block_number](./core-starknet-testing-set_block_number.md) | Sets the block number to the provided value.[...](./core-starknet-testing-set_block_number.md) |
| [set_caller_address](./core-starknet-testing-set_caller_address.md) | Sets the caller address to the provided value.[...](./core-starknet-testing-set_caller_address.md) |
| [set_contract_address](./core-starknet-testing-set_contract_address.md) | Sets the contract address to the provided value.[...](./core-starknet-testing-set_contract_address.md) |
| [set_sequencer_address](./core-starknet-testing-set_sequencer_address.md) | Sets the sequencer address to the provided value.[...](./core-starknet-testing-set_sequencer_address.md) |
| [set_block_timestamp](./core-starknet-testing-set_block_timestamp.md) | Sets the block timestamp to the provided value.[...](./core-starknet-testing-set_block_timestamp.md) |
| [set_version](./core-starknet-testing-set_version.md) | Sets the version to the provided value.[...](./core-starknet-testing-set_version.md) |
| [set_account_contract_address](./core-starknet-testing-set_account_contract_address.md) | Sets the account contract address.[...](./core-starknet-testing-set_account_contract_address.md) |
| [set_max_fee](./core-starknet-testing-set_max_fee.md) | Sets the transaction max fee.[...](./core-starknet-testing-set_max_fee.md) |
| [set_transaction_hash](./core-starknet-testing-set_transaction_hash.md) | Sets the transaction hash.[...](./core-starknet-testing-set_transaction_hash.md) |
| [set_chain_id](./core-starknet-testing-set_chain_id.md) | Set the transaction chain id.[...](./core-starknet-testing-set_chain_id.md) |
| [set_nonce](./core-starknet-testing-set_nonce.md) | Set the transaction nonce.[...](./core-starknet-testing-set_nonce.md) |
| [set_signature](./core-starknet-testing-set_signature.md) | Set the transaction signature.[...](./core-starknet-testing-set_signature.md) |
| [set_block_hash](./core-starknet-testing-set_block_hash.md) | Set the hash for a block.[...](./core-starknet-testing-set_block_hash.md) |
| [pop_log_raw](./core-starknet-testing-pop_log_raw.md) | Pop the earliest unpopped logged event for the contract.[...](./core-starknet-testing-pop_log_raw.md) |
| [pop_log](./core-starknet-testing-pop_log.md) | Pop the earliest unpopped logged event for the contract as the requested type.[...](./core-starknet-testing-pop_log.md) |
| [pop_l2_to_l1_message](./core-starknet-testing-pop_l2_to_l1_message.md) | Pop the earliest unpopped l2 to l1 message for the contract.[...](./core-starknet-testing-pop_l2_to_l1_message.md) |

[Extern functions](./core-starknet-testing-extern_functions.md)
 ---
| | |
|:---|:---|
| [cheatcode](./core-starknet-testing-cheatcode.md) | A general cheatcode function used to simplify implementation of Starknet testing functions. This is the base function used by testing utilities to interact with the test[...](./core-starknet-testing-cheatcode.md) |
