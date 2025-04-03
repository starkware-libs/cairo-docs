# max

Takes two comparable values `a` and `b` and returns the greatest of the two values.  # Examples
```cairo
use core::cmp::max;

assert!(max(0, 1) == 1);
```

Fully qualified path: `core::cmp::max`

```rust
pub fn max<T, +PartialOrd<T>, +Drop<T>, +Copy<T>>(a: T, b: T) -> T
```

