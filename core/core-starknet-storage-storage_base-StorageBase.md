# StorageBase

A struct for holding an address to initialize a storage path with. The members (not direct members, but accessible using deref) of a contract state are either `StorageBase` or `FlattenedStorage` instances, with the generic type representing the type of the stored member.

Fully qualified path: `core::starknet::storage::storage_base::StorageBase`

```rust
pub struct StorageBase<T> {
    pub __base_address__: felt252,
}
```

