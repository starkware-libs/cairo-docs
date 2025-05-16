# u256_mul_mod_n

Returns `a * b (mod n)`.  # Examples
```cairo
use core::math::u256_mul_mod_n;

let result = u256_mul_mod_n(17, 23, 29);
assert!(result == 14);
```

Fully qualified path: `core::math::u256_mul_mod_n`

<pre><code class="language-rust">pub fn u256_mul_mod_n(a: u256, b: u256, n: NonZero&lt;u256&gt;) -&gt; u256</code></pre>

