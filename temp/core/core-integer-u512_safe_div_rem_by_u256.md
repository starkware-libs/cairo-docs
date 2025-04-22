# u512_safe_div_rem_by_u256

Calculates division with remainder of a u512 by a non-zero u256.

Fully qualified path: `core::integer::u512_safe_div_rem_by_u256`

```rust
pub fn u512_safe_div_rem_by_u256(
    lhs: u512, rhs: NonZero<u256>,
) -> (u512, u256) implicits(RangeCheck) nopanic
```

