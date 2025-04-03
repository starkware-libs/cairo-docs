# StorageTrait

A trait for creating the struct containing the StorageBase or FlattenedStorage of all the members of a contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait`

```rust
pub trait StorageTrait<T>
```

## Trait functions

### storage

Creates a struct containing the StorageBase or FlattenedStorage of all the members of a contract state. Should be called from the `deref` method of the contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait::storage`

```rust
fn storage(self: FlattenedStorage<T>) -> Self::BaseType
```


## Trait types

### BaseType

The type of the struct containing the StorageBase or FlattenedStorage of all the members of a the type `T`.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait::BaseType`

```rust
type BaseType;
```


