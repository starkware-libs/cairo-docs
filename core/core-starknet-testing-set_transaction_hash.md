# set_transaction_hash

Sets the transaction hash.  # Arguments  `hash` - The transaction hash to set.  After a call to `set_transaction_hash`, `starknet::get_execution_info().tx_info.transaction_hash` will return the set value.

Fully qualified path: `core::starknet::testing::set_transaction_hash`

```rust
pub fn set_transaction_hash(hash: felt252)
```

