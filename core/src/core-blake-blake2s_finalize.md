# blake2s_finalize

Similar to `blake2s_compress`, but used for the final block of the message.

Fully qualified path: `core::blake::blake2s_finalize`

<pre><code class="language-rust">pub extern fn blake2s_finalize(
    state: Blake2sState, byte_count: u32, msg: Blake2sInput,
) -&gt; Blake2sState nopanic;</code></pre>

