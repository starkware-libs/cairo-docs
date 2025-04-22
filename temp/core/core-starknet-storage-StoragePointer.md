# StoragePointer

A pointer to an address in storage, can be used to read and write values, if the generic type supports it (e.g. basic types like `felt252`).

Fully qualified path: `core::starknet::storage::StoragePointer`

```rust
pub struct StoragePointer<T> {
    pub __storage_pointer_address__: StorageBaseAddress,
    pub __storage_pointer_offset__: u8,
}
```

