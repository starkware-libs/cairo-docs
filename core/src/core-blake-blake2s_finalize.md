# blake2s_finalize

Similar to `blake2s_compress`, but used for the final block of the message.

Fully qualified path: [core](./core.md)::[blake](./core-blake.md)::[blake2s_finalize](./core-blake-blake2s_finalize.md)

<pre><code class="language-cairo">pub extern fn blake2s_finalize(state: <a href="core-box-Box.html">Box&lt;u32; 8]&gt;</a>, byte_count: <a href="core-integer-u32.html">u32</a>, msg: <a href="core-box-Box.html">Box&lt;u32; 16]&gt;</a>) -&gt; <a href="core-box-Box.html">Box&lt;u32; 8]&gt;</a> nopanic;</code></pre>

