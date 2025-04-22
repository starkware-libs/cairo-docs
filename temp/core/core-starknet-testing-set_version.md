# set_version

Sets the version to the provided value.  # Arguments  `version` - The version to set.  After a call to `set_version`, `starknet::get_execution_info().tx_info.version` will return the set value.

Fully qualified path: `core::starknet::testing::set_version`

```rust
pub fn set_version(version: felt252)
```

