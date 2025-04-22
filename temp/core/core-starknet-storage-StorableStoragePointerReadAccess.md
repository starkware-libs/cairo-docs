# StorableStoragePointerReadAccess

Simple implementation of `StoragePointerReadAccess` for any type that implements `Store` for any offset.

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess`

```rust
pub impl StorableStoragePointerReadAccess<
    T, +starknet::Store<T>,
> of StoragePointerReadAccess<StoragePointer<T>>
```

## Impl functions

### read

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess::read`

```rust
fn read(self: @StoragePointer<T>) -> T
```


## Impl types

### Value

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess::Value`

```rust
type Value = T;
```


