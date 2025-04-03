# WrappingMul

Performs multiplication that wraps around on overflow.  # Examples
```cairo
use core::num::traits::WrappingMul;

let result = 10_u8.wrapping_mul(30);
assert!(result == 44); // (10 * 30) % 256 = 44

let result = 200_u8.wrapping_mul(2);
assert!(result == 144); // (200 * 2) % 256 = 144
```

Fully qualified path: `core::num::traits::ops::wrapping::WrappingMul`

```rust
pub trait WrappingMul<T>
```

## Trait functions

### wrapping_mul

Wrapping (modular) multiplication. Computes `self * other`, wrapping around at the boundary of the type.

Fully qualified path: `core::num::traits::ops::wrapping::WrappingMul::wrapping_mul`

```rust
fn wrapping_mul(self: T, v: T) -> T
```


