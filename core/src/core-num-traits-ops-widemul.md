# widemul

Trait for performing multiplication that results in a wider type.
This module provides the `WideMul` trait which enables multiplication operations
that return a result type with double the bit width of the input types.
This is particularly useful when you need to perform multiplication without
worrying about overflow, as the result type can hold the full range of possible values.
# Examples

```cairo
use core::num::traits::WideMul;

// Multiplying two `u8` values to get a `u16` result
let a: u8 = 200;
let b: u8 = 100;
let result: u16 = a.wide_mul(b);
assert!(result == 20000);

// Multiplying two `u128` values to get a `u256` result
let x: u128 = 0xffffffffffffffffffffffffffffffff; // max u128
let y: u128 = 2;
let wide_result = x.wide_mul(y); // No overflow occurs
assert!(wide_result == 0x01fffffffffffffffffffffffffffffffe);
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

Fully qualified path: [core](./core.md)::[num](./core-num.md)::[traits](./core-num-traits.md)::[ops](./core-num-traits-ops.md)::[widemul](./core-num-traits-ops-widemul.md)


[Traits](./core-num-traits-ops-widemul-traits.md)
 ---
| | |
|:---|:---|
| [WideMul](./core-num-traits-ops-widemul-WideMul.md) | A trait for types that can be multiplied together to produce a wider type. This trait enables multiplication operations where the result type has double[...](./core-num-traits-ops-widemul-WideMul.md) |
