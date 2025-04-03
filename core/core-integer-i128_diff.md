# i128_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**128 + lhs - rhs)`.

Fully qualified path: `core::integer::i128_diff`

```rust
pub extern fn i128_diff(lhs: i128, rhs: i128) -> Result<u128, u128> implicits(RangeCheck) nopanic;
```

