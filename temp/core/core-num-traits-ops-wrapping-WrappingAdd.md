# WrappingAdd

Performs addition that wraps around on overflow.  # Examples
```cairo
use core::num::traits::WrappingAdd;

let result = 255_u8.wrapping_add(1);
assert!(result == 0);

let result = 100_u8.wrapping_add(200);
assert!(result == 44); // (100 + 200) % 256 = 44
```

Fully qualified path: `core::num::traits::ops::wrapping::WrappingAdd`

```rust
pub trait WrappingAdd<T>
```

## Trait functions

### wrapping_add

Wrapping (modular) addition. Computes `self + other`, wrapping around at the boundary of the type.

Fully qualified path: `core::num::traits::ops::wrapping::WrappingAdd::wrapping_add`

```rust
fn wrapping_add(self: T, v: T) -> T
```


