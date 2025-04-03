# testing

Module for starknet testing only. Provides functions useful for testing event emission, starknet state information, and the cheatcode concept in general. Testing utilities for Starknet contracts.  This module provides functions for testing Starknet contracts. The functions allow manipulation of blockchain state and storage variables during tests, as well as inspection of emitted events and messages.  Note: The functions in this module can only be used with the `cairo-test` testing framework. If you are using Starknet Foundry, refer to its [https://foundry-rs.github.io/starknet-foundry/appendix/cheatcodes.html]([documentation](https://foundry-rs.github.io/starknet-foundry/appendix/cheatcodes.html)).

Fully qualified path: `core::starknet::testing`

## Free functions

- [set_block_number](./core-starknet-testing-set_block_number.md)

- [set_caller_address](./core-starknet-testing-set_caller_address.md)

- [set_contract_address](./core-starknet-testing-set_contract_address.md)

- [set_sequencer_address](./core-starknet-testing-set_sequencer_address.md)

- [set_block_timestamp](./core-starknet-testing-set_block_timestamp.md)

- [set_version](./core-starknet-testing-set_version.md)

- [set_account_contract_address](./core-starknet-testing-set_account_contract_address.md)

- [set_max_fee](./core-starknet-testing-set_max_fee.md)

- [set_transaction_hash](./core-starknet-testing-set_transaction_hash.md)

- [set_chain_id](./core-starknet-testing-set_chain_id.md)

- [set_nonce](./core-starknet-testing-set_nonce.md)

- [set_signature](./core-starknet-testing-set_signature.md)

- [set_block_hash](./core-starknet-testing-set_block_hash.md)

- [pop_log_raw](./core-starknet-testing-pop_log_raw.md)

- [pop_log](./core-starknet-testing-pop_log.md)

- [pop_l2_to_l1_message](./core-starknet-testing-pop_l2_to_l1_message.md)

## Extern functions

- [cheatcode](./core-starknet-testing-cheatcode.md)

