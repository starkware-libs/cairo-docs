# EcStateTrait

Fully qualified path: `core::ec::EcStateTrait`

```rust
pub trait EcStateTrait
```

## Trait functions

### init

Initializes an EC computation with the zero point.

Fully qualified path: `core::ec::EcStateTrait::init`

```rust
fn init() -> EcState nopanic
```


### add

Adds a point to the computation.

Fully qualified path: `core::ec::EcStateTrait::add`

```rust
fn add(ref self: EcState, p: NonZeroEcPoint) nopanic
```


### sub

Subs a point to the computation.

Fully qualified path: `core::ec::EcStateTrait::sub`

```rust
fn sub(ref self: EcState, p: NonZeroEcPoint)
```


### add_mul

Adds the product p * scalar to the state.

Fully qualified path: `core::ec::EcStateTrait::add_mul`

```rust
fn add_mul(ref self: EcState, scalar: felt252, p: NonZeroEcPoint) nopanic
```


### finalize_nz

Finalizes the EC computation and returns the result (returns `None` if the result is the zero point).

Fully qualified path: `core::ec::EcStateTrait::finalize_nz`

```rust
fn finalize_nz(self: EcState) -> Option<NonZeroEcPoint> nopanic
```


### finalize

Finalizes the EC computation and returns the result.

Fully qualified path: `core::ec::EcStateTrait::finalize`

```rust
fn finalize(self: EcState) -> EcPoint
```


