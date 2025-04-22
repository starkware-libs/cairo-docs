# Secp256r1Impl

Fully qualified path: `core::starknet::secp256r1::Secp256r1Impl`

```rust
pub(crate) impl Secp256r1Impl of Secp256Trait<Secp256r1Point>
```

## Impl functions

### get_curve_size

Fully qualified path: `core::starknet::secp256r1::Secp256r1Impl::get_curve_size`

```rust
fn get_curve_size() -> u256
```


### get_generator_point

Fully qualified path: `core::starknet::secp256r1::Secp256r1Impl::get_generator_point`

```rust
fn get_generator_point() -> Secp256r1Point
```


### secp256_ec_new_syscall

Fully qualified path: `core::starknet::secp256r1::Secp256r1Impl::secp256_ec_new_syscall`

```rust
fn secp256_ec_new_syscall(x: u256, y: u256) -> SyscallResult<Option<Secp256r1Point>>
```


### secp256_ec_get_point_from_x_syscall

Fully qualified path: `core::starknet::secp256r1::Secp256r1Impl::secp256_ec_get_point_from_x_syscall`

```rust
fn secp256_ec_get_point_from_x_syscall(
    x: u256, y_parity: bool,
) -> SyscallResult<Option<Secp256r1Point>>
```


