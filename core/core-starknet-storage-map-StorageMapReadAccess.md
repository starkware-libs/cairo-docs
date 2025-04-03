# StorageMapReadAccess

Trait for reading a contract/component storage member in a specific key place.

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess`

```rust
pub trait StorageMapReadAccess<TMemberState>
```

## Trait functions

### read

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::read`

```rust
fn read(self: TMemberState, key: Self::Key) -> Self::Value
```


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::Key`

```rust
type Key;
```


### Value

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::Value`

```rust
type Value;
```


