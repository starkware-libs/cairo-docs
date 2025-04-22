# StorageTraitMut

A trait for creating the struct containing the mutable StorageBase or FlattenedStorage of all the members of a contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut`

```rust
pub trait StorageTraitMut<T>
```

## Trait functions

### storage_mut

Creates a struct containing a mutable version of the the StorageBase or FlattenedStorage of all the members of a contract state. Should be called from the `deref` method of the contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut::storage_mut`

```rust
fn storage_mut(self: FlattenedStorage<Mutable<T>>) -> Self::BaseType
```


## Trait types

### BaseType

The type of the struct containing the mutable StorageBase or FlattenedStorage of all the members of a the type `T`.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut::BaseType`

```rust
type BaseType;
```


