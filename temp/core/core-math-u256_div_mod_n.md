# u256_div_mod_n

Returns `a / b (mod n)`, or `None` if `b` is not invertible modulo `n`.  # Examples
```cairo
use core::math::u256_inv_mod;

let result = u256_div_mod_n(17, 7, 29);
assert!(result == Option::Some(19));
```

Fully qualified path: `core::math::u256_div_mod_n`

```rust
pub fn u256_div_mod_n(a: u256, b: u256, n: NonZero<u256>) -> Option<u256>
```

