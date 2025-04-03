# u32_safe_divmod

Fully qualified path: `core::integer::u32_safe_divmod`

```rust
pub extern fn u32_safe_divmod(
    lhs: u32, rhs: NonZero<u32>,
) -> (u32, u32) implicits(RangeCheck) nopanic;
```

