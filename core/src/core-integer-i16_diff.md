# i16_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**16 + lhs - rhs)`.

Fully qualified path: `core::integer::i16_diff`

<pre><code class="language-rust">pub extern fn i16_diff(lhs: i16, rhs: i16) -&gt; Result&lt;u16, u16&gt; implicits(RangeCheck) nopanic;</code></pre>

