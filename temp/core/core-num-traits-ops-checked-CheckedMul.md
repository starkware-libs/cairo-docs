# CheckedMul

Performs multiplication that returns `None` instead of wrapping around on underflow or overflow.

Fully qualified path: `core::num::traits::ops::checked::CheckedMul`

```rust
pub trait CheckedMul<T>
```

## Trait functions

### checked_mul

Multiplies two numbers, checking for underflow or overflow. If underflow or overflow happens, `None` is returned.

Fully qualified path: `core::num::traits::ops::checked::CheckedMul::checked_mul`

```rust
fn checked_mul(self: T, v: T) -> Option<T>
```


