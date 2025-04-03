# SubPointersMut

A mutable version of `SubPointers`, works the same way, but on `Mutable<T>`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut`

```rust
pub trait SubPointersMut<T>
```

## Trait functions

### sub_pointers_mut

Creates a sub pointers struct for the given storage pointer to a struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut::sub_pointers_mut`

```rust
fn sub_pointers_mut(self: StoragePointer<Mutable<T>>) -> Self::SubPointersType
```


## Trait types

### SubPointersType

The type of the storage pointers, generated for the struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut::SubPointersType`

```rust
type SubPointersType;
```


