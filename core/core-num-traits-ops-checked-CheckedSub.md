# CheckedSub

Performs subtraction that returns `None` instead of wrapping around on underflow.

Fully qualified path: `core::num::traits::ops::checked::CheckedSub`

```rust
pub trait CheckedSub<T>
```

## Trait functions

### checked_sub

Subtracts two numbers, checking for underflow. If underflow happens, `None` is returned.

Fully qualified path: `core::num::traits::ops::checked::CheckedSub::checked_sub`

```rust
fn checked_sub(self: T, v: T) -> Option<T>
```


