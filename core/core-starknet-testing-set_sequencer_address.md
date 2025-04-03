# set_sequencer_address

Sets the sequencer address to the provided value.  # Arguments  `address` - The sequencer address to set.  After a call to `set_sequencer_address`, `starknet::get_execution_info().block_info.sequencer_address` will return the set value.

Fully qualified path: `core::starknet::testing::set_sequencer_address`

```rust
pub fn set_sequencer_address(address: ContractAddress)
```

