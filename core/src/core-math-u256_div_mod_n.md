# u256_div_mod_n

Returns `a / b (mod n)`, or `None` if `b` is not invertible modulo `n`.  # Examples
```cairo
use core::math::u256_inv_mod;

let result = u256_div_mod_n(17, 7, 29);
assert!(result == Some(19));
```

Fully qualified path: `core::math::u256_div_mod_n`

<pre><code class="language-rust">pub fn u256_div_mod_n(a: u256, b: u256, n: NonZero&lt;u256&gt;) -&gt; Option&lt;u256&gt;</code></pre>

