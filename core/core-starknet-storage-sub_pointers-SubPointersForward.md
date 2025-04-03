# SubPointersForward

A trait for implementing `SubPointers` for types which are not a `StoragePointer`, such as `StorageBase` and `StoragePath`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward`

```rust
pub trait SubPointersForward<T>
```

## Trait functions

### sub_pointers

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward::sub_pointers`

```rust
fn sub_pointers(self: T) -> Self::SubPointersType
```


## Trait types

### SubPointersType

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward::SubPointersType`

```rust
type SubPointersType;
```


