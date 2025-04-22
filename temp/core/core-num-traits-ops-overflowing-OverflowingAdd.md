# OverflowingAdd

Performs addition with a flag for overflow.  # Examples
```cairo
use core::num::traits::OverflowingAdd;

let (result, is_overflow) = 1_u8.overflowing_add(255_u8);
assert!(result == 0);
assert!(is_overflow);
```

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingAdd`

```rust
pub trait OverflowingAdd<T>
```

## Trait functions

### overflowing_add

Returns a tuple of the sum along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingAdd::overflowing_add`

```rust
fn overflowing_add(self: T, v: T) -> (T, bool)
```


