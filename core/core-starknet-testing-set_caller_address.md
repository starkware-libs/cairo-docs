# set_caller_address

Sets the caller address to the provided value.  # Arguments  `address` - The caller address to set.  After a call to `set_caller_address`, `starknet::get_execution_info().caller_address` will return the set value.

Fully qualified path: `core::starknet::testing::set_caller_address`

```rust
pub fn set_caller_address(address: ContractAddress)
```

