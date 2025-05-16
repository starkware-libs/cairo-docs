# ByteArrayIter

An iterator struct over a ByteArray.

Fully qualified path: `core::byte_array::ByteArrayIter`

<pre><code class="language-rust">#[derive(Drop, Clone)]
pub struct ByteArrayIter {
    ba: ByteArray,
    current_index: crate::ops::RangeIterator&lt;usize&gt;,
}</code></pre>

