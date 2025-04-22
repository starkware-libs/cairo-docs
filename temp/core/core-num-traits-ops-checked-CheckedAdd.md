# CheckedAdd

Performs addition that returns `None` instead of wrapping around on overflow.

Fully qualified path: `core::num::traits::ops::checked::CheckedAdd`

```rust
pub trait CheckedAdd<T>
```

## Trait functions

### checked_add

Adds two numbers, checking for overflow. If overflow happens, `None` is returned.

Fully qualified path: `core::num::traits::ops::checked::CheckedAdd::checked_add`

```rust
fn checked_add(self: T, v: T) -> Option<T>
```


