# PendingStoragePathTrait

A trait for creating a `PendingStoragePath` from a hash state and a key.

Fully qualified path: `core::starknet::storage::PendingStoragePathTrait`

```rust
pub trait PendingStoragePathTrait<T, S>
```

## Trait functions

### new

Fully qualified path: `core::starknet::storage::PendingStoragePathTrait::new`

```rust
fn new(storage_path: @StoragePath<S>, pending_key: felt252) -> PendingStoragePath<T>
```


