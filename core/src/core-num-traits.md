# traits

Fully qualified path: [core](./core.md)::[num](./core-num.md)::[traits](./core-num-traits.md)


[Modules](./core-num-traits-modules.md)
 ---
| | |
|:---|:---|
| [zero](./core-num-traits-zero.md) | Traits for types with an additive identity element.[...](./core-num-traits-zero.md) |
| [one](./core-num-traits-one.md) | Traits for types with a multiplicative identity element.[...](./core-num-traits-one.md) |
| [bit_size](./core-num-traits-bit_size.md) | Utilities for determining the bit size of types.[...](./core-num-traits-bit_size.md) |
| [ops](./core-num-traits-ops.md) | [...](./core-num-traits-ops.md) |
| [bounded](./core-num-traits-bounded.md) | Defines minimum and maximum values for numeric types.[...](./core-num-traits-bounded.md) |
## Re-exports

 - ### Traits

| | |
|:---|:---|
| [Zero](./core-num-traits-zero-Zero.md) | Defines an additive identity element for `T` .[...](./core-num-traits-zero-Zero.md) |
| [One](./core-num-traits-one-One.md) | Defines a multiplicative identity element for `T` .[...](./core-num-traits-one-One.md) |
| [BitSize](./core-num-traits-bit_size-BitSize.md) | A trait used to retrieve the size of a type in bits.[...](./core-num-traits-bit_size-BitSize.md) |
| [Bounded](./core-num-traits-bounded-Bounded.md) | A trait defining minimum and maximum bounds for numeric types. This trait only supports types that can have constant values.[...](./core-num-traits-bounded-Bounded.md) |
| [CheckedAdd](./core-num-traits-ops-checked-CheckedAdd.md) | Performs addition that returns `None`  instead of wrapping around on overflow.[...](./core-num-traits-ops-checked-CheckedAdd.md) |
| [CheckedMul](./core-num-traits-ops-checked-CheckedMul.md) | Performs multiplication that returns `None`  instead of wrapping around on underflow or overflow.[...](./core-num-traits-ops-checked-CheckedMul.md) |
| [CheckedSub](./core-num-traits-ops-checked-CheckedSub.md) | Performs subtraction that returns `None`  instead of wrapping around on underflow.[...](./core-num-traits-ops-checked-CheckedSub.md) |
| [DivRem](./core-num-traits-ops-divrem-DivRem.md) | Performs truncated division and  remainder. `T`  – dividend type (left-hand operand) `U`  – divisor  type (right-hand operand, must be wrapped in `NonZero<U>`  at call-site)[...](./core-num-traits-ops-divrem-DivRem.md) |
| [OverflowingAdd](./core-num-traits-ops-overflowing-OverflowingAdd.md) | Performs addition with a flag for overflow.[...](./core-num-traits-ops-overflowing-OverflowingAdd.md) |
| [OverflowingMul](./core-num-traits-ops-overflowing-OverflowingMul.md) | Performs multiplication with a flag for overflow.[...](./core-num-traits-ops-overflowing-OverflowingMul.md) |
| [OverflowingSub](./core-num-traits-ops-overflowing-OverflowingSub.md) | Performs subtraction with a flag for overflow.[...](./core-num-traits-ops-overflowing-OverflowingSub.md) |
| [Pow](./core-num-traits-ops-pow-Pow.md) | Raises a value to the power of `exp` . Note that `0⁰`  ( `pow(0, 0)` ) returns `1` . Mathematically this is undefined.[...](./core-num-traits-ops-pow-Pow.md) |
| [SaturatingAdd](./core-num-traits-ops-saturating-SaturatingAdd.md) | Performs addition that saturates at the numeric bounds instead of overflowing.[...](./core-num-traits-ops-saturating-SaturatingAdd.md) |
| [SaturatingMul](./core-num-traits-ops-saturating-SaturatingMul.md) | Performs multiplication that saturates at the numeric bounds instead of overflowing.[...](./core-num-traits-ops-saturating-SaturatingMul.md) |
| [SaturatingSub](./core-num-traits-ops-saturating-SaturatingSub.md) | Performs subtraction that saturates at the numeric bounds instead of overflowing.[...](./core-num-traits-ops-saturating-SaturatingSub.md) |
| [Sqrt](./core-num-traits-ops-sqrt-Sqrt.md) | A trait for computing the square root of a number.[...](./core-num-traits-ops-sqrt-Sqrt.md) |
| [WideMul](./core-num-traits-ops-widemul-WideMul.md) | A trait for types that can be multiplied together to produce a wider type. This trait enables multiplication operations where the result type has double[...](./core-num-traits-ops-widemul-WideMul.md) |
| [WideSquare](./core-num-traits-ops-widesquare-WideSquare.md) | A trait for a type that can be squared to produce a wider type. This trait enables squaring operations where the result type has double[...](./core-num-traits-ops-widesquare-WideSquare.md) |
| [WrappingAdd](./core-num-traits-ops-wrapping-WrappingAdd.md) | Performs addition that wraps around on overflow.[...](./core-num-traits-ops-wrapping-WrappingAdd.md) |
| [WrappingMul](./core-num-traits-ops-wrapping-WrappingMul.md) | Performs multiplication that wraps around on overflow.[...](./core-num-traits-ops-wrapping-WrappingMul.md) |
| [WrappingSub](./core-num-traits-ops-wrapping-WrappingSub.md) | Performs subtraction that wraps around on overflow.[...](./core-num-traits-ops-wrapping-WrappingSub.md) |

<br>

