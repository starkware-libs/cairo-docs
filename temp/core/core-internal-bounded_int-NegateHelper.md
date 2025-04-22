# NegateHelper

A helper trait for negating a `BoundedInt` instance.

Fully qualified path: `core::internal::bounded_int::NegateHelper`

```rust
pub trait NegateHelper<T>
```

## Trait functions

### negate

Negates the given value.

Fully qualified path: `core::internal::bounded_int::NegateHelper::negate`

```rust
fn negate(self: T) -> Self::Result
```


### negate_nz

Negates the given non-zero value.

Fully qualified path: `core::internal::bounded_int::NegateHelper::negate_nz`

```rust
fn negate_nz(self: NonZero<T>) -> NonZero<Self::Result>
```


## Trait types

### Result

The result of negating the given value.

Fully qualified path: `core::internal::bounded_int::NegateHelper::Result`

```rust
type Result;
```


