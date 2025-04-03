# i16_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**16 + lhs - rhs)`.

Fully qualified path: `core::integer::i16_diff`

```rust
pub extern fn i16_diff(lhs: i16, rhs: i16) -> Result<u16, u16> implicits(RangeCheck) nopanic;
```

