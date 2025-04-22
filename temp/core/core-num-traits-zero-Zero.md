# Zero

Defines an additive identity element for `T`.  # Laws
```text
a + 0 = a       ∀ a ∈ T
0 + a = a       ∀ a ∈ T
```

Fully qualified path: `core::num::traits::zero::Zero`

```rust
pub trait Zero<T>
```

## Trait functions

### zero

Returns the additive identity element of `T`, `0`.  # Examples
```cairo
use core::num::traits::Zero;

assert!(Zero::<u32>::zero() == 0);
```

Fully qualified path: `core::num::traits::zero::Zero::zero`

```rust
fn zero() -> T
```


### is_zero

Returns true if `self` is equal to the additive identity.  # Examples
```cairo
use core::num::traits::Zero;

assert!(0.is_zero());
assert!(!5.is_zero());
```

Fully qualified path: `core::num::traits::zero::Zero::is_zero`

```rust
fn is_zero(self: @T) -> bool
```


### is_non_zero

Returns false if `self` is equal to the additive identity.  # Examples
```cairo
use core::num::traits::Zero;

assert!(5.is_non_zero());
assert!(!0.is_non_zero());
```

Fully qualified path: `core::num::traits::zero::Zero::is_non_zero`

```rust
fn is_non_zero(self: @T) -> bool
```


