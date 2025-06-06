# widesquare

Wide square operation.
This module provides the `WideSquare` trait which enables squaring operations
that return a result type with double the bit width of the input type.
This is particularly useful when you need to square a number without
worrying about overflow, as the result type can hold the full range of possible values.
# Examples

```cairo
use core::num::traits::WideSquare;

// Squaring a `u8` value to get a `u16` result
let a: u8 = 200;
let result: u16 = a.wide_square();
assert!(result == 40000);

// Squaring a `u128` value to get a `u256` result
let x: u128 = 0xffffffffffffffffffffffffffffffff; // max u128
let wide_result: u256 = x.wide_square(); // No overflow occurs
assert!(wide_result == 0xfffffffffffffffffffffffffffffffe00000000000000000000000000000001);
```
# Available Implementations

The trait is implemented for the following type pairs:
- `i8` → `i16`
- `i16` → `i32`
- `i32` → `i64`
- `i64` → `i128`
- `u8` → `u16`
- `u16` → `u32`
- `u32` → `u64`
- `u64` → `u128`
- `u128` → `u256`
- `u256` → `u512`

Fully qualified path: [core](./core.md)::[num](./core-num.md)::[traits](./core-num-traits.md)::[ops](./core-num-traits-ops.md)::[widesquare](./core-num-traits-ops-widesquare.md)


[Traits](./core-num-traits-ops-widesquare-traits.md)
 ---
| | |
|:---|:---|
| [WideSquare](./core-num-traits-ops-widesquare-WideSquare.md) | A trait for a type that can be squared to produce a wider type. This trait enables squaring operations where the result type has double[...](./core-num-traits-ops-widesquare-WideSquare.md) |
