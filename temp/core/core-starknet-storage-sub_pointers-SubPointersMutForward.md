# SubPointersMutForward

A trait for implementing `SubPointersMut` for types which are not a `StoragePointer`, such as `StorageBase` and `StoragePath`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward`

```rust
pub trait SubPointersMutForward<T>
```

## Trait functions

### sub_pointers_mut

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward::sub_pointers_mut`

```rust
fn sub_pointers_mut(self: T) -> Self::SubPointersType
```


## Trait types

### SubPointersType

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward::SubPointersType`

```rust
type SubPointersType;
```


