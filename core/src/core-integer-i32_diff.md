# i32_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**32 + lhs - rhs)`.

Fully qualified path: `core::integer::i32_diff`

<pre><code class="language-rust">pub extern fn i32_diff(lhs: i32, rhs: i32) -&gt; Result&lt;u32, u32&gt; implicits(RangeCheck) nopanic;</code></pre>

