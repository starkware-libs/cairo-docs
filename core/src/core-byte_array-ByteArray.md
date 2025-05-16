# ByteArray

Byte array type.

Fully qualified path: `core::byte_array::ByteArray`

<pre><code class="language-rust">#[derive(Drop, Clone, PartialEq, Serde, Default)]
pub struct ByteArray {
    pub(crate) data: Array&lt;bytes31&gt;,
    pub(crate) pending_word: felt252,
    pub(crate) pending_word_len: usize,
}</code></pre>

