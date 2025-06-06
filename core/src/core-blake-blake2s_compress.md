# blake2s_compress

The blake2s compress function, which takes a state, a byte count, and a message, and returns a
new state.
`byte_count` should be the total number of bytes hashed after hashing the current `msg`.

Fully qualified path: [core](./core.md)::[blake](./core-blake.md)::[blake2s_compress](./core-blake-blake2s_compress.md)

<pre><code class="language-cairo">pub extern fn blake2s_compress(state: <a href="core-box-Box.html">Box&lt;u32; 8]&gt;</a>, byte_count: <a href="core-integer-u32.html">u32</a>, msg: <a href="core-box-Box.html">Box&lt;u32; 16]&gt;</a>) -&gt; <a href="core-box-Box.html">Box&lt;u32; 8]&gt;</a> nopanic;</code></pre>

