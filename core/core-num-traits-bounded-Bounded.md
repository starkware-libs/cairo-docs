# Bounded

A trait defining minimum and maximum bounds for numeric types.  This trait only supports types that can have constant values.

Fully qualified path: `core::num::traits::bounded::Bounded`

```rust
pub trait Bounded<T>
```

## Trait constants

### MIN

Returns the minimum value for type `T`.  # Examples
```cairo
use core::num::traits::Bounded;

let min = Bounded::<u8>::MIN;
assert!(min == 0);
```

Fully qualified path: `core::num::traits::bounded::Bounded::MIN`

```rust
const MIN: T;
```


### MAX

Returns the maximum value for type `T`.  # Examples
```cairo
use core::num::traits::Bounded;

let max = Bounded::<u8>::MAX;
assert!(max == 255);
```

Fully qualified path: `core::num::traits::bounded::Bounded::MAX`

```rust
const MAX: T;
```


