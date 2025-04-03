# u16_safe_divmod

Fully qualified path: `core::integer::u16_safe_divmod`

```rust
pub extern fn u16_safe_divmod(
    lhs: u16, rhs: NonZero<u16>,
) -> (u16, u16) implicits(RangeCheck) nopanic;
```

