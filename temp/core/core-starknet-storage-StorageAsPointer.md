# StorageAsPointer

Trait for converting a storage member to a `StoragePointer0Offset`.

Fully qualified path: `core::starknet::storage::StorageAsPointer`

```rust
pub trait StorageAsPointer<TMemberState>
```

## Trait functions

### as_ptr

Fully qualified path: `core::starknet::storage::StorageAsPointer::as_ptr`

```rust
fn as_ptr(self: @TMemberState) -> StoragePointer0Offset<Self::Value>
```


## Trait types

### Value

Fully qualified path: `core::starknet::storage::StorageAsPointer::Value`

```rust
type Value;
```


