# Secp256r1PointImpl

Fully qualified path: `core::starknet::secp256r1::Secp256r1PointImpl`

```rust
pub(crate) impl Secp256r1PointImpl of Secp256PointTrait<Secp256r1Point>
```

## Impl functions

### get_coordinates

Fully qualified path: `core::starknet::secp256r1::Secp256r1PointImpl::get_coordinates`

```rust
fn get_coordinates(self: Secp256r1Point) -> SyscallResult<(u256, u256)>
```


### add

Fully qualified path: `core::starknet::secp256r1::Secp256r1PointImpl::add`

```rust
fn add(self: Secp256r1Point, other: Secp256r1Point) -> SyscallResult<Secp256r1Point>
```


### mul

Fully qualified path: `core::starknet::secp256r1::Secp256r1PointImpl::mul`

```rust
fn mul(self: Secp256r1Point, scalar: u256) -> SyscallResult<Secp256r1Point>
```


