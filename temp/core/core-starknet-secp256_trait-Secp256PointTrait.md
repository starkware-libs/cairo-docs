# Secp256PointTrait

Fully qualified path: `core::starknet::secp256_trait::Secp256PointTrait`

```rust
pub trait Secp256PointTrait<Secp256Point>
```

## Trait functions

### get_coordinates

Fully qualified path: `core::starknet::secp256_trait::Secp256PointTrait::get_coordinates`

```rust
fn get_coordinates(self: Secp256Point) -> SyscallResult<(u256, u256)>
```


### add

Fully qualified path: `core::starknet::secp256_trait::Secp256PointTrait::add`

```rust
fn add(self: Secp256Point, other: Secp256Point) -> SyscallResult<Secp256Point>
```


### mul

Fully qualified path: `core::starknet::secp256_trait::Secp256PointTrait::mul`

```rust
fn mul(self: Secp256Point, scalar: u256) -> SyscallResult<Secp256Point>
```


