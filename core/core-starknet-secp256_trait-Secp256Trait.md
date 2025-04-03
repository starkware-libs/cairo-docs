# Secp256Trait

Fully qualified path: `core::starknet::secp256_trait::Secp256Trait`

```rust
pub trait Secp256Trait<Secp256Point>
```

## Trait functions

### get_curve_size

Fully qualified path: `core::starknet::secp256_trait::Secp256Trait::get_curve_size`

```rust
fn get_curve_size() -> u256
```


### get_generator_point

Fully qualified path: `core::starknet::secp256_trait::Secp256Trait::get_generator_point`

```rust
fn get_generator_point() -> Secp256Point
```


### secp256_ec_new_syscall

Fully qualified path: `core::starknet::secp256_trait::Secp256Trait::secp256_ec_new_syscall`

```rust
fn secp256_ec_new_syscall(x: u256, y: u256) -> SyscallResult<Option<Secp256Point>>
```


### secp256_ec_get_point_from_x_syscall

Fully qualified path: `core::starknet::secp256_trait::Secp256Trait::secp256_ec_get_point_from_x_syscall`

```rust
fn secp256_ec_get_point_from_x_syscall(
    x: u256, y_parity: bool,
) -> SyscallResult<Option<Secp256Point>>
```


