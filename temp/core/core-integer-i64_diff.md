# i64_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**64 + lhs - rhs)`.

Fully qualified path: `core::integer::i64_diff`

```rust
pub extern fn i64_diff(lhs: i64, rhs: i64) -> Result<u64, u64> implicits(RangeCheck) nopanic;
```

