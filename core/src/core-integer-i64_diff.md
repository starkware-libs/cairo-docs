# i64_diff

If `lhs` >= `rhs` returns `Ok(lhs - rhs)` else returns `Err(2**64 + lhs - rhs)`.

Fully qualified path: `core::integer::i64_diff`

<pre><code class="language-rust">pub extern fn i64_diff(lhs: i64, rhs: i64) -&gt; Result&lt;u64, u64&gt; implicits(RangeCheck) nopanic;</code></pre>

