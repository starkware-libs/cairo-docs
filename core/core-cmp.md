# cmp

Module for comparison operations. Utilities for comparing and ordering values. This module contains functions that rely on the `PartialOrd` trait for comparing values.  # Examples
```cairo
use core::cmp::{min, max, minmax};

assert!(min(10, 20) == 10);
assert!(max(10, 20) == 20);

assert!(minmax(20, 10) == (10, 20));
assert!(minmax(10, 20) == (10, 20));
```

Fully qualified path: `core::cmp`

## Free functions

- [min](./core-cmp-min.md)

- [max](./core-cmp-max.md)

- [minmax](./core-cmp-minmax.md)

