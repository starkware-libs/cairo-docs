# Sqrt

A trait for computing the square root of a number.  # Examples
```cairo
use core::num::traits::Sqrt;

assert!(9_u8.sqrt() == 3);
```

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt`

```rust
pub trait Sqrt<T>
```

## Trait functions

### sqrt

Computes the square root of a number.

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt::sqrt`

```rust
fn sqrt(self: T) -> Self::Target
```


## Trait types

### Target

The type of the result of the square root operation.

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt::Target`

```rust
type Target;
```


