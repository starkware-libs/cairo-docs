# integer

Integer types and operations.This module provides the built-in integer types and their associated operations.  # Integer TypesThe following integer types are available:Unsigned integers: [`u8`](./core-integer-u8.md), [`u16`](./core-integer-u16.md), [`u32`](./core-integer-u32.md), [`u64`](./core-integer-u64.md), [`u128`](./core-integer-u128.md), [`u256`](./core-integer-u256.md) * Signed integers: [`i8`](./core-integer-i8.md), [`i16`](./core-integer-i16.md), [`i32`](./core-integer-i32.md), [`i64`](./core-integer-i64.md), [`i128`](./core-integer-i128.md)  # OperationsInteger types implement various traits that enable common operations:Basic arithmetic via [`Add`](./core-traits-Add.md), [`Sub`](./core-traits-Sub.md), [`Mul`](./core-traits-Mul.md), [`Div`](./core-traits-Div.md), [`Rem`](./core-traits-Rem.md) and [`DivRem`](./core-traits-DivRem.md) * Bitwise operations via [`BitAnd`](./core-traits-BitAnd.md), [`BitOr`](./core-traits-BitOr.md), [`BitXor`](./core-traits-BitXor.md), and [`BitNot`](./core-traits-BitNot.md) * Comparison via [`PartialEq`](./core-traits-PartialEq.md) and [`PartialOrd`](./core-traits-PartialOrd.md) * Safe arithmetic via [`CheckedAdd`](`CheckedAdd`), [`CheckedSub`](`CheckedSub`), [`CheckedMul`](`CheckedMul`) * Wrapping arithmetic via [`WrappingAdd`](`WrappingAdd`), [`WrappingSub`](`WrappingSub`), [`WrappingMul`](`WrappingMul`) * Overflow handling via [`OverflowingAdd`](`OverflowingAdd`), [`OverflowingSub`](`OverflowingSub`), [`OverflowingMul`](`OverflowingMul`)[`Add`](./core-traits-Add.md): crate::traits::Add [`Sub`](./core-traits-Sub.md): crate::traits::Sub [`Mul`](./core-traits-Mul.md): crate::traits::Mul [`Div`](./core-traits-Div.md): crate::traits::Div [`Rem`](./core-traits-Rem.md): crate::traits::Rem [`DivRem`](./core-traits-DivRem.md): crate::traits::DivRem [`CheckedAdd`](`CheckedAdd`): crate::num::traits::ops::checked::CheckedAdd [`CheckedSub`](`CheckedSub`): crate::num::traits::ops::checked::CheckedSub [`CheckedMul`](`CheckedMul`): crate::num::traits::ops::checked::CheckedMul [`WrappingAdd`](`WrappingAdd`): crate::num::traits::ops::wrapping::WrappingAdd [`WrappingSub`](`WrappingSub`): crate::num::traits::ops::wrapping::WrappingSub [`WrappingMul`](`WrappingMul`): crate::num::traits::ops::wrapping::WrappingMul [`OverflowingAdd`](`OverflowingAdd`): crate::num::traits::ops::overflowing::OverflowingAdd [`OverflowingSub`](`OverflowingSub`): crate::num::traits::ops::overflowing::OverflowingSub [`OverflowingMul`](`OverflowingMul`): crate::num::traits::ops::overflowing::OverflowingMul  # ExamplesBasic operators:
```cairo
let a: u8 = 5;
let b: u8 = 10;
assert_eq!(a + b, 15);
assert_eq!(a * b, 50);
assert_eq!(a & b, 0);
assert!(a < b);
```
Checked operations:
```cairo
use core::num::traits::{CheckedAdd, Bounded};

let max: u8 = Bounded::MAX;
assert!(max.checked_add(1_u8).is_none());
```
  # ConversionsIntegers can be converted between different types using:[`TryInto`](./core-traits-TryInto.md) for potentially fallible conversions * [`Into`](./core-traits-Into.md) for infallible conversions to wider types

Fully qualified path: `core::integer`

## Free functions

- [u128_wrapping_add](./core-integer-u128_wrapping_add.md)

- [u128_wrapping_sub](./core-integer-u128_wrapping_sub.md)

- [u128_wide_mul](./core-integer-u128_wide_mul.md)

- [u128_overflowing_mul](./core-integer-u128_overflowing_mul.md)

- [u8_wrapping_add](./core-integer-u8_wrapping_add.md)

- [u8_wrapping_sub](./core-integer-u8_wrapping_sub.md)

- [u16_wrapping_add](./core-integer-u16_wrapping_add.md)

- [u16_wrapping_sub](./core-integer-u16_wrapping_sub.md)

- [u32_wrapping_add](./core-integer-u32_wrapping_add.md)

- [u32_wrapping_sub](./core-integer-u32_wrapping_sub.md)

- [u64_wrapping_add](./core-integer-u64_wrapping_add.md)

- [u64_wrapping_sub](./core-integer-u64_wrapping_sub.md)

- [u256_overflowing_add](./core-integer-u256_overflowing_add.md)

- [u256_overflowing_sub](./core-integer-u256_overflowing_sub.md)

- [u256_overflow_sub](./core-integer-u256_overflow_sub.md)

- [u256_overflowing_mul](./core-integer-u256_overflowing_mul.md)

- [u256_overflow_mul](./core-integer-u256_overflow_mul.md)

- [u256_wide_mul](./core-integer-u256_wide_mul.md)

- [u512_safe_div_rem_by_u256](./core-integer-u512_safe_div_rem_by_u256.md)

## Structs

- [u256](./core-integer-u256.md)

- [u512](./core-integer-u512.md)

## Traits

- [NumericLiteral](./core-integer-NumericLiteral.md)

- [BoundedInt](./core-integer-BoundedInt.md)

## Extern types

- [u128](./core-integer-u128.md)

- [U128MulGuarantee](./core-integer-U128MulGuarantee.md)

- [Bitwise](./core-integer-Bitwise.md)

- [u8](./core-integer-u8.md)

- [u16](./core-integer-u16.md)

- [u32](./core-integer-u32.md)

- [u64](./core-integer-u64.md)

- [i8](./core-integer-i8.md)

- [i16](./core-integer-i16.md)

- [i32](./core-integer-i32.md)

- [i64](./core-integer-i64.md)

- [i128](./core-integer-i128.md)

## Extern functions

- [u128_overflowing_add](./core-integer-u128_overflowing_add.md)

- [u128_overflowing_sub](./core-integer-u128_overflowing_sub.md)

- [u128_sqrt](./core-integer-u128_sqrt.md)

- [u128_safe_divmod](./core-integer-u128_safe_divmod.md)

- [u128_byte_reverse](./core-integer-u128_byte_reverse.md)

- [u8_overflowing_add](./core-integer-u8_overflowing_add.md)

- [u8_overflowing_sub](./core-integer-u8_overflowing_sub.md)

- [u8_wide_mul](./core-integer-u8_wide_mul.md)

- [u8_sqrt](./core-integer-u8_sqrt.md)

- [u8_safe_divmod](./core-integer-u8_safe_divmod.md)

- [u16_overflowing_add](./core-integer-u16_overflowing_add.md)

- [u16_overflowing_sub](./core-integer-u16_overflowing_sub.md)

- [u16_wide_mul](./core-integer-u16_wide_mul.md)

- [u16_sqrt](./core-integer-u16_sqrt.md)

- [u16_safe_divmod](./core-integer-u16_safe_divmod.md)

- [u32_overflowing_add](./core-integer-u32_overflowing_add.md)

- [u32_overflowing_sub](./core-integer-u32_overflowing_sub.md)

- [u32_wide_mul](./core-integer-u32_wide_mul.md)

- [u32_sqrt](./core-integer-u32_sqrt.md)

- [u32_safe_divmod](./core-integer-u32_safe_divmod.md)

- [u64_overflowing_add](./core-integer-u64_overflowing_add.md)

- [u64_overflowing_sub](./core-integer-u64_overflowing_sub.md)

- [u64_wide_mul](./core-integer-u64_wide_mul.md)

- [u64_sqrt](./core-integer-u64_sqrt.md)

- [u64_safe_divmod](./core-integer-u64_safe_divmod.md)

- [u256_sqrt](./core-integer-u256_sqrt.md)

- [i8_wide_mul](./core-integer-i8_wide_mul.md)

- [i8_diff](./core-integer-i8_diff.md)

- [i16_wide_mul](./core-integer-i16_wide_mul.md)

- [i16_diff](./core-integer-i16_diff.md)

- [i32_wide_mul](./core-integer-i32_wide_mul.md)

- [i32_diff](./core-integer-i32_diff.md)

- [i64_wide_mul](./core-integer-i64_wide_mul.md)

- [i64_diff](./core-integer-i64_diff.md)

- [i128_diff](./core-integer-i128_diff.md)

