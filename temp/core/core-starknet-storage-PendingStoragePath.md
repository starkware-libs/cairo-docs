# PendingStoragePath

A struct for delaying the creation of a storage path, used for lazy evaluation in storage nodes.

Fully qualified path: `core::starknet::storage::PendingStoragePath`

```rust
pub struct PendingStoragePath<T> {
    __hash_state__: StoragePathHashState,
    __pending_key__: felt252,
}
```

