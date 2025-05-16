# i8_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**8 + lhs - rhs)`.

Fully qualified path: `core::integer::i8_diff`

<pre><code class="language-rust">pub extern fn i8_diff(lhs: i8, rhs: i8) -&gt; Result&lt;u8, u8&gt; implicits(RangeCheck) nopanic;</code></pre>

