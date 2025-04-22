# set_block_timestamp

Sets the block timestamp to the provided value.  # Arguments  `block_timestamp` - The block timestamp to set.  After a call to `set_block_timestamp`, `starknet::get_execution_info().block_info.block_timestamp` will return the set value.

Fully qualified path: `core::starknet::testing::set_block_timestamp`

```rust
pub fn set_block_timestamp(block_timestamp: u64)
```

