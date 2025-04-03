# minmax

Takes two comparable values `a` and `b` and returns a tuple with the smallest value and the greatest value.  # Examples
```cairo
use core::cmp::minmax;

assert!(minmax(0, 1) == (0, 1));
assert!(minmax(1, 0) == (0, 1));
```

Fully qualified path: `core::cmp::minmax`

```rust
pub fn minmax<T, +PartialOrd<T>, +Drop<T>, +Copy<T>>(a: T, b: T) -> (T, T)
```

