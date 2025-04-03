# Vec

A type to represent a vec in storage. The length of the storage is stored in the storage base, while the elements are stored in hash(storage_base, index).

Fully qualified path: `core::starknet::storage::vec::Vec`

```rust
#[phantom]
pub struct Vec<T> {}
```

