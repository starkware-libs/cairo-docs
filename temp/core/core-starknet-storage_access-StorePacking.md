# StorePacking

Trait for easier implementation of `Store` used for packing and unpacking values into values that already implement `Store`, and having `Store` implemented using this conversion.

Fully qualified path: `core::starknet::storage_access::StorePacking`

```rust
pub trait StorePacking<T, PackedT>
```

## Trait functions

### pack

Packs a value of type `T` into a value of type `PackedT`.

Fully qualified path: `core::starknet::storage_access::StorePacking::pack`

```rust
fn pack(value: T) -> PackedT
```


### unpack

Unpacks a value of type `PackedT` into a value of type `T`.

Fully qualified path: `core::starknet::storage_access::StorePacking::unpack`

```rust
fn unpack(value: PackedT) -> T
```


