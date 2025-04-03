# SaturatingMul

Performs multiplication that saturates at the numeric bounds instead of overflowing.  # Examples
```cairo
use core::num::traits::SaturatingMul;

assert!(100_u8.saturating_mul(3_u8) == 255);
```

Fully qualified path: `core::num::traits::ops::saturating::SaturatingMul`

```rust
pub trait SaturatingMul<T>
```

## Trait functions

### saturating_mul

Saturating multiplication. Computes `self * other`, saturating at the relevant high or low boundary of the type.

Fully qualified path: `core::num::traits::ops::saturating::SaturatingMul::saturating_mul`

```rust
fn saturating_mul(self: T, other: T) -> T
```


