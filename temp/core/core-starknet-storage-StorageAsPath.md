# StorageAsPath

Trait for creating a new `StoragePath` from a storage member.

Fully qualified path: `core::starknet::storage::StorageAsPath`

```rust
pub trait StorageAsPath<TMemberState>
```

## Trait functions

### as_path

Fully qualified path: `core::starknet::storage::StorageAsPath::as_path`

```rust
fn as_path(self: @TMemberState) -> StoragePath<Self::Value>
```


## Trait types

### Value

Fully qualified path: `core::starknet::storage::StorageAsPath::Value`

```rust
type Value;
```


