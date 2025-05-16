# checked

Safe arithmetic operations with overflow/underflow checking.This module provides traits for performing arithmetic operations with explicit overflow and underflow protection. These operations return `None` when an overflow or underflow occurs, allowing you to handle these cases gracefully without panicking.  # Examples
```cairo
use core::num::traits::{CheckedAdd, CheckedSub, CheckedMul};

// Checked addition
let a: u8 = 1;
assert!(a.checked_add(2) == Some(3));
assert!(a.checked_add(255) == None); // Overflow

// Checked subtraction
let b: u8 = 1;
assert!(b.checked_sub(1) == Some(0));
assert!(b.checked_sub(2) == None); // Underflow

// Checked multiplication
let c: u8 = 10;
assert!(c.checked_mul(20) == Some(200));
assert!(c.checked_mul(30) == None); // Overflow
```

Fully qualified path: `core::num::traits::ops::checked`

## Traits

- [CheckedAdd](./core-num-traits-ops-checked-CheckedAdd.md)

- [CheckedSub](./core-num-traits-ops-checked-CheckedSub.md)

- [CheckedMul](./core-num-traits-ops-checked-CheckedMul.md)

