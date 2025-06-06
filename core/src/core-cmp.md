# cmp

Utilities for comparing and ordering values.
This module contains functions that rely on the `PartialOrd` trait for comparing values.
# Examples

```cairo
use core::cmp::{min, max, minmax};

assert!(min(10, 20) == 10);
assert!(max(10, 20) == 20);

assert!(minmax(20, 10) == (10, 20));
assert!(minmax(10, 20) == (10, 20));
```

Fully qualified path: [core](./core.md)::[cmp](./core-cmp.md)


[Free functions](./core-cmp-free_functions.md)
 ---
| | |
|:---|:---|
| [min](./core-cmp-min.md) | Takes two comparable values `a`  and `b`  and returns the smaller of the two values.[...](./core-cmp-min.md) |
| [max](./core-cmp-max.md) | Takes two comparable values `a`  and `b`  and returns the greater of the two values.[...](./core-cmp-max.md) |
| [minmax](./core-cmp-minmax.md) | Takes two comparable values `a`  and `b`  and returns a tuple with the smaller value and the greater value.[...](./core-cmp-minmax.md) |
