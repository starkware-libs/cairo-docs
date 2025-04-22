# one_shift_left_bytes_felt252

Returns `1 << (8 * n_bytes)` as `felt252`, assuming that `n_bytes < BYTES_IN_BYTES31`.  Note: if `n_bytes >= BYTES_IN_BYTES31`, the behavior is undefined. If one wants to assert that in the callsite, it's sufficient to assert that `n_bytes != BYTES_IN_BYTES31` because if `n_bytes > 31` then `n_bytes - 16 > 15` and `one_shift_left_bytes_u128` would panic.

Fully qualified path: `core::bytes_31::one_shift_left_bytes_felt252`

```rust
pub(crate) fn one_shift_left_bytes_felt252(n_bytes: usize) -> felt252
```

