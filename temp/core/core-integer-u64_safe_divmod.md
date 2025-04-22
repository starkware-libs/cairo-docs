# u64_safe_divmod

Fully qualified path: `core::integer::u64_safe_divmod`

```rust
pub extern fn u64_safe_divmod(
    lhs: u64, rhs: NonZero<u64>,
) -> (u64, u64) implicits(RangeCheck) nopanic;
```

