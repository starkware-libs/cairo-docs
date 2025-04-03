# StorageNodeMut

A mutable version of `StorageNode`, works the same way, but on `Mutable<T>`.

Fully qualified path: `core::starknet::storage::storage_node::StorageNodeMut`

```rust
pub trait StorageNodeMut<T>
```

## Trait functions

### storage_node_mut

Fully qualified path: `core::starknet::storage::storage_node::StorageNodeMut::storage_node_mut`

```rust
fn storage_node_mut(self: StoragePath<Mutable<T>>) -> Self::NodeType
```


## Trait types

### NodeType

Fully qualified path: `core::starknet::storage::storage_node::StorageNodeMut::NodeType`

```rust
type NodeType;
```


