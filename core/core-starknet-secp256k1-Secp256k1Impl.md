# Secp256k1Impl

Fully qualified path: `core::starknet::secp256k1::Secp256k1Impl`

```rust
pub(crate) impl Secp256k1Impl of Secp256Trait<Secp256k1Point>
```

## Impl functions

### get_curve_size

Fully qualified path: `core::starknet::secp256k1::Secp256k1Impl::get_curve_size`

```rust
fn get_curve_size() -> u256
```


### get_generator_point

Fully qualified path: `core::starknet::secp256k1::Secp256k1Impl::get_generator_point`

```rust
fn get_generator_point() -> Secp256k1Point
```


### secp256_ec_new_syscall

Fully qualified path: `core::starknet::secp256k1::Secp256k1Impl::secp256_ec_new_syscall`

```rust
fn secp256_ec_new_syscall(x: u256, y: u256) -> SyscallResult<Option<Secp256k1Point>>
```


### secp256_ec_get_point_from_x_syscall

Fully qualified path: `core::starknet::secp256k1::Secp256k1Impl::secp256_ec_get_point_from_x_syscall`

```rust
fn secp256_ec_get_point_from_x_syscall(
    x: u256, y_parity: bool,
) -> SyscallResult<Option<Secp256k1Point>>
```


