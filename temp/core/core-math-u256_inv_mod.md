# u256_inv_mod

Returns the inverse of `a` modulo `n`, or `None` if `a` is not invertible modulo `n`.  All `a`s will be considered not invertible for `n == 1`.  # Examples
```cairo
use core::math::u256_inv_mod;

let inv = u256_inv_mod(3, 17);
assert!(inv == Option::Some(6));
```

Fully qualified path: `core::math::u256_inv_mod`

```rust
pub fn u256_inv_mod(a: u256, n: NonZero<u256>) -> Option<NonZero<u256>>
```

