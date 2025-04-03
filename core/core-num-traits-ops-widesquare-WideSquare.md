# WideSquare

A trait for a type that can be squared to produce a wider type.  This trait enables squaring operations where the result type has double the bit width of the input type, preventing overflow in cases where the result would exceed the input type's maximum value.  # Examples
```cairo
use core::num::traits::WideSquare;

let a: u8 = 16;
let result: u16 = a.wide_square();
assert!(result == 256);
```

Fully qualified path: `core::num::traits::ops::widesquare::WideSquare`

```rust
pub trait WideSquare<T>
```

## Trait functions

### wide_square

Calculates the square, producing a wider type.

Fully qualified path: `core::num::traits::ops::widesquare::WideSquare::wide_square`

```rust
fn wide_square(self: T) -> Self::Target
```


## Trait types

### Target

The type of the result of the square.

Fully qualified path: `core::num::traits::ops::widesquare::WideSquare::Target`

```rust
type Target;
```


