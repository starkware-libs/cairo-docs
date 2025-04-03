# Secp256k1PointImpl

Fully qualified path: `core::starknet::secp256k1::Secp256k1PointImpl`

```rust
pub(crate) impl Secp256k1PointImpl of Secp256PointTrait<Secp256k1Point>
```

## Impl functions

### get_coordinates

Fully qualified path: `core::starknet::secp256k1::Secp256k1PointImpl::get_coordinates`

```rust
fn get_coordinates(self: Secp256k1Point) -> SyscallResult<(u256, u256)>
```


### add

Fully qualified path: `core::starknet::secp256k1::Secp256k1PointImpl::add`

```rust
fn add(self: Secp256k1Point, other: Secp256k1Point) -> SyscallResult<Secp256k1Point>
```


### mul

Fully qualified path: `core::starknet::secp256k1::Secp256k1PointImpl::mul`

```rust
fn mul(self: Secp256k1Point, scalar: u256) -> SyscallResult<Secp256k1Point>
```


