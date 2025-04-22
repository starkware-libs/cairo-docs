# OverflowingMul

Performs multiplication with a flag for overflow.  # Examples
```cairo
use core::num::traits::OverflowingMul;

let (result, is_overflow) = 1_u8.overflowing_mul(2_u8);
assert!(result == 2);
assert!(!is_overflow);
```

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingMul`

```rust
pub trait OverflowingMul<T>
```

## Trait functions

### overflowing_mul

Returns a tuple of the product along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingMul::overflowing_mul`

```rust
fn overflowing_mul(self: T, v: T) -> (T, bool)
```


