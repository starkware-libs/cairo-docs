# u128_safe_divmod

Fully qualified path: `core::integer::u128_safe_divmod`

```rust
pub extern fn u128_safe_divmod(
    lhs: u128, rhs: NonZero<u128>,
) -> (u128, u128) implicits(RangeCheck) nopanic;
```

