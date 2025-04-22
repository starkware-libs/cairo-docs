# SaturatingAdd

Performs addition that saturates at the numeric bounds instead of overflowing.  # Examples
```cairo
use core::num::traits::SaturatingAdd;

assert!(255_u8.saturating_add(1_u8) == 255);
```

Fully qualified path: `core::num::traits::ops::saturating::SaturatingAdd`

```rust
pub trait SaturatingAdd<T>
```

## Trait functions

### saturating_add

Saturating addition. Computes `self + other`, saturating at the relevant high or low boundary of the type.

Fully qualified path: `core::num::traits::ops::saturating::SaturatingAdd::saturating_add`

```rust
fn saturating_add(self: T, other: T) -> T
```


