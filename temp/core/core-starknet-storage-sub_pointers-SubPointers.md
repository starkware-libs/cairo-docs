# SubPointers

Similar to storage node, but for structs which are stored sequentially in the storage. In contrast to storage node, the fields of the struct are just offsetted from the base address of the struct.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers`

```rust
pub trait SubPointers<T>
```

## Trait functions

### sub_pointers

Creates a sub pointers struct for the given storage pointer to a struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers::sub_pointers`

```rust
fn sub_pointers(self: StoragePointer<T>) -> Self::SubPointersType
```


## Trait types

### SubPointersType

The type of the storage pointers, generated for the struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers::SubPointersType`

```rust
type SubPointersType;
```


