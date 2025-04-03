# StorageMapWriteAccess

Trait for writing contract/component storage member in a specific key place.

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess`

```rust
pub trait StorageMapWriteAccess<TMemberState>
```

## Trait functions

### write

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::write`

```rust
fn write(self: TMemberState, key: Self::Key, value: Self::Value)
```


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::Key`

```rust
type Key;
```


### Value

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::Value`

```rust
type Value;
```


