# egcd

Computes the extended GCD and Bezout coefficients for two numbers.  Uses the Extended Euclidean algorithm to find (g, s, t, sub_direction) where `g = gcd(a, b)`. The relationship between inputs and outputs is: * If `sub_direction` is true:  `g = s * a - t * b` * If `sub_direction` is false: `g = t * b - s * a`  Returns a tuple (g, s, t, sub_direction) where g is the GCD and `(s, -t)` or `(-s, t)` are the Bezout coefficients (according to `sub_direction`).  # Examples
```cairo
use core::math::egcd;

let (g, s, t, dir) = egcd::<u32>(12, 8);
assert!(g == 4);
```

Fully qualified path: `core::math::egcd`

```rust
pub fn egcd<
    T,
    +Copy<T>,
    +Drop<T>,
    +Add<T>,
    +Mul<T>,
    +DivRem<T>,
    +core::num::traits::Zero<T>,
    +core::num::traits::One<T>,
    +TryInto<T, NonZero<T>>,
>(
    a: NonZero<T>, b: NonZero<T>,
) -> (T, T, T, bool)
```

