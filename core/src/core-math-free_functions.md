
[Free functions](./core-math-free_functions.md)
 ---
| | |
|:---|:---|
| [egcd](./core-math-egcd.md) | Computes the extended GCD and Bezout coefficients for two numbers. Uses the Extended Euclidean algorithm to find (g, s, t, sub_direction) where `g = gcd(a, b)` .[...](./core-math-egcd.md) |
| [inv_mod](./core-math-inv_mod.md) | Computes the modular multiplicative inverse of `a`  modulo `n` . Returns `s`  such that `a*s ≡ 1 (mod n)`  where `s`  is between `1`  and `n-1`  inclusive, or `None`  if `gcd(a,n) > 1`[...](./core-math-inv_mod.md) |
| [u256_inv_mod](./core-math-u256_inv_mod.md) | Returns the inverse of `a`  modulo `n` , or `None`  if `a`  is not invertible modulo `n` . All `a` s will be considered not invertible for `n == 1` .[...](./core-math-u256_inv_mod.md) |
| [u256_div_mod_n](./core-math-u256_div_mod_n.md) | Returns `a / b (mod n)` , or `None`  if `b`  is not invertible modulo `n` .[...](./core-math-u256_div_mod_n.md) |
| [u256_mul_mod_n](./core-math-u256_mul_mod_n.md) | Returns `a * b (mod n)` .[...](./core-math-u256_mul_mod_n.md) |
