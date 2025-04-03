# one_shift_left_bytes_u128

Returns `1 << (8 * n_bytes)` as `u128`, where `n_bytes` must be < `BYTES_IN_U128`.  Panics if `n_bytes >= BYTES_IN_U128`.

Fully qualified path: `core::bytes_31::one_shift_left_bytes_u128`

```rust
pub(crate) fn one_shift_left_bytes_u128(n_bytes: usize) -> u128
```

