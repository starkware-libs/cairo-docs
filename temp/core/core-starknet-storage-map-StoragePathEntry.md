# StoragePathEntry

Trait for updating the hash state with a value, using an `entry` method.

Fully qualified path: `core::starknet::storage::map::StoragePathEntry`

```rust
pub trait StoragePathEntry<C>
```

## Trait functions

### entry

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::entry`

```rust
fn entry(self: C, key: Self::Key) -> StoragePath<Self::Value>
```


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::Key`

```rust
type Key;
```


### Value

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::Value`

```rust
type Value;
```


