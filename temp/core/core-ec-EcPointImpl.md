# EcPointImpl

Fully qualified path: `core::ec::EcPointImpl`

```rust
pub impl EcPointImpl of EcPointTrait
```

## Impl functions

### new

Creates a new EC point from its (x, y) coordinates.

Fully qualified path: `core::ec::EcPointImpl::new`

```rust
fn new(x: felt252, y: felt252) -> Option<EcPoint>
```


### new_nz

Creates a new NonZero EC point from its (x, y) coordinates.

Fully qualified path: `core::ec::EcPointImpl::new_nz`

```rust
fn new_nz(x: felt252, y: felt252) -> Option<NonZeroEcPoint>
```


### new_from_x

Creates a new EC point from its x coordinate.

Fully qualified path: `core::ec::EcPointImpl::new_from_x`

```rust
fn new_from_x(x: felt252) -> Option<EcPoint>
```


### new_nz_from_x

Creates a new NonZero EC point from its x coordinate.

Fully qualified path: `core::ec::EcPointImpl::new_nz_from_x`

```rust
fn new_nz_from_x(x: felt252) -> Option<NonZeroEcPoint>
```


### coordinates

Returns the coordinates of the EC point.

Fully qualified path: `core::ec::EcPointImpl::coordinates`

```rust
fn coordinates(self: NonZeroEcPoint) -> (felt252, felt252)
```


### x

Returns the x coordinate of the EC point.

Fully qualified path: `core::ec::EcPointImpl::x`

```rust
fn x(self: NonZeroEcPoint) -> felt252
```


### y

Returns the y coordinate of the EC point.

Fully qualified path: `core::ec::EcPointImpl::y`

```rust
fn y(self: NonZeroEcPoint) -> felt252
```


### mul

Computes the product of an EC point `p` by the given scalar `scalar`.

Fully qualified path: `core::ec::EcPointImpl::mul`

```rust
fn mul(self: EcPoint, scalar: felt252) -> EcPoint
```


