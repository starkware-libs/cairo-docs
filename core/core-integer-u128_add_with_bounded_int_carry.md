# u128_add_with_bounded_int_carry

Helper function for implementation of `u256_wide_mul`. Used for adding two u128s and receiving a BoundedInt for the carry result.

Fully qualified path: `core::integer::u128_add_with_bounded_int_carry`

```rust
pub(crate) fn u128_add_with_bounded_int_carry(
    a: u128, b: u128,
) -> (u128, crate::internal::bounded_int::BoundedInt<0, 1>) nopanic
```

