# ByteArrayIter

An iterator struct over a ByteArray.

Fully qualified path: [core](./core.md)::[byte_array](./core-byte_array.md)::[ByteArrayIter](./core-byte_array-ByteArrayIter.md)

<pre><code class="language-cairo">#[derive(Drop, Clone)]
pub struct ByteArrayIter {
    ba: <a href="core-byte_array-ByteArray.html">ByteArray</a>,
    current_index: <a href="core-ops-range-internal-IntRange.html">IntRange&lt;u32&gt;</a>,
}</code></pre>

