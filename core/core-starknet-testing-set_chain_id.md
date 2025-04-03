# set_chain_id

Set the transaction chain id.  # Arguments  `chain_id` - The chain id to set.  After a call to `set_chain_id`, `starknet::get_execution_info().tx_info.chain_id` will return the set value.

Fully qualified path: `core::starknet::testing::set_chain_id`

```rust
pub fn set_chain_id(chain_id: felt252)
```

