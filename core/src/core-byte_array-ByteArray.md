# ByteArray

Byte array type.

Fully qualified path: [core](./core.md)::[byte_array](./core-byte_array.md)::[ByteArray](./core-byte_array-ByteArray.md)

<pre><code class="language-cairo">#[derive(Drop, Clone, PartialEq, Serde, Default)]
pub struct ByteArray {
    pub(crate) data: <a href="core-array-Array.html">Array&lt;bytes31&gt;</a>,
    pub(crate) pending_word: <a href="core-felt252.html">felt252</a>,
    pub(crate) pending_word_len: <a href="core-integer-u32.html">u32</a>,
}</code></pre>

