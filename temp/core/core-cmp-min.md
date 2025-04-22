# min

Takes two comparable values `a` and `b` and returns the smallest of the two values.  # Examples
```cairo
use core::cmp::min;

assert!(min(0, 1) == 0);
```

Fully qualified path: `core::cmp::min`

```rust
pub fn min<T, +PartialOrd<T>, +Drop<T>, +Copy<T>>(a: T, b: T) -> T
```

