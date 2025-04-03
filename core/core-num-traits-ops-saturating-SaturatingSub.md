# SaturatingSub

Performs subtraction that saturates at the numeric bounds instead of overflowing.  # Examples
```cairo
use core::num::traits::SaturatingSub;

assert!(1_u8.saturating_sub(2_u8) == 0);
```

Fully qualified path: `core::num::traits::ops::saturating::SaturatingSub`

```rust
pub trait SaturatingSub<T>
```

## Trait functions

### saturating_sub

Saturating subtraction. Computes `self - other`, saturating at the relevant high or low boundary of the type.

Fully qualified path: `core::num::traits::ops::saturating::SaturatingSub::saturating_sub`

```rust
fn saturating_sub(self: T, other: T) -> T
```


