# set_block_number

Sets the block number to the provided value.  # Arguments  `block_number` - The block number to set.  After a call to `set_block_number`, `starknet::get_execution_info().block_info.block_number` will return the set value.

Fully qualified path: `core::starknet::testing::set_block_number`

```rust
pub fn set_block_number(block_number: u64)
```

