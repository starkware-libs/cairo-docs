# wrapping

Arithmetic operations with overflow and underflow wrapping.  This module provides traits for performing arithmetic operations that wrap around at the boundary of the type in case of overflow or underflow. This is particularly useful when you want to: - Perform arithmetic operations without panicking on overflow/underflow - Implement modular arithmetic - Handle cases where overflow is expected and desired  # Examples
```cairo
use core::num::traits::{WrappingAdd, WrappingSub, WrappingMul};

// Addition wrapping
let a: u8 = 255;
assert!(a.wrapping_add(1) == 0);

// Subtraction wrapping
let b: u8 = 0;
assert!(b.wrapping_sub(1) == 255);

// Multiplication wrapping
let c: u8 = 200;
assert!(c.wrapping_mul(2) == 144); // (200 * 2) % 256 = 144
```

Fully qualified path: `core::num::traits::ops::wrapping`

## Modules

- [overflow_based](./core-num-traits-ops-wrapping-overflow_based.md)

## Traits

- [WrappingAdd](./core-num-traits-ops-wrapping-WrappingAdd.md)

- [WrappingSub](./core-num-traits-ops-wrapping-WrappingSub.md)

- [WrappingMul](./core-num-traits-ops-wrapping-WrappingMul.md)

