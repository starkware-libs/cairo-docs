# inv_mod

Computes the modular multiplicative inverse of `a` modulo `n`.  Returns `s` such that `a*s ≡ 1 (mod n)` where `s` is between `1` and `n-1` inclusive, or `Option::None` if `gcd(a,n) > 1` (inverse doesn't exist).  # Examples
```cairo
use core::math::inv_mod;

let inv = inv_mod::<u32>(3, 7);
assert!(inv == Option::Some(5));
```

Fully qualified path: `core::math::inv_mod`

```rust
pub fn inv_mod<
    T,
    +Copy<T>,
    +Drop<T>,
    +Add<T>,
    +Sub<T>,
    +Mul<T>,
    +DivRem<T>,
    +core::num::traits::Zero<T>,
    +core::num::traits::One<T>,
    +TryInto<T, NonZero<T>>,
>(
    a: NonZero<T>, n: NonZero<T>,
) -> Option<T>
```

