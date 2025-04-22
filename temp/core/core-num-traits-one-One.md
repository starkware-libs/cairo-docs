# One

Defines a multiplicative identity element for `T`.  # Laws
```text
a * 1 = a       ∀ a ∈ T
1 * a = a       ∀ a ∈ T
```

Fully qualified path: `core::num::traits::one::One`

```rust
pub trait One<T>
```

## Trait functions

### one

Returns the multiplicative identity element of `T`, `1`.  # Examples
```cairo
use core::num::traits::One;

assert!(One::<u32>::one() == 1);
```

Fully qualified path: `core::num::traits::one::One::one`

```rust
fn one() -> T
```


### is_one

Returns true if `self` is equal to the multiplicative identity.  # Examples
```cairo
use core::num::traits::One;

assert!(1.is_one());
assert!(!0.is_one());
```

Fully qualified path: `core::num::traits::one::One::is_one`

```rust
fn is_one(self: @T) -> bool
```


### is_non_one

Returns false if `self` is equal to the multiplicative identity.  # Examples
```cairo
use core::num::traits::One;

assert!(0.is_non_one());
assert!(!1.is_non_one());
```

Fully qualified path: `core::num::traits::one::One::is_non_one`

```rust
fn is_non_one(self: @T) -> bool
```


