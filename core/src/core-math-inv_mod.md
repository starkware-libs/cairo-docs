# inv_mod

Computes the modular multiplicative inverse of `a` modulo `n`.Returns `s` such that `a*s ≡ 1 (mod n)` where `s` is between `1` and `n-1` inclusive, or `None` if `gcd(a,n) > 1` (inverse doesn't exist).  # Examples
```cairo
use core::math::inv_mod;

let inv = inv_mod::<u32>(3, 7);
assert!(inv == Some(5));
```

Fully qualified path: `core::math::inv_mod`

<pre><code class="language-rust">pub fn inv_mod&lt;
    T,
    +Copy&lt;T&gt;,
    +Drop&lt;T&gt;,
    +Add&lt;T&gt;,
    +Sub&lt;T&gt;,
    +Mul&lt;T&gt;,
    +DivRem&lt;T&gt;,
    +core::num::traits::Zero&lt;T&gt;,
    +core::num::traits::One&lt;T&gt;,
    +TryInto&lt;T, NonZero&lt;T&gt;&gt;,
&gt;(
    a: NonZero&lt;T&gt;, n: NonZero&lt;T&gt;,
) -&gt; Option&lt;T&gt;</code></pre>

