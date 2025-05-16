# blake2s_compress

The blake2s compress function, which takes a state, a byte count, and a message, and returns a new state. `byte_count` should be the total number of bytes hashed after hashing the current `msg`.

Fully qualified path: `core::blake::blake2s_compress`

<pre><code class="language-rust">pub extern fn blake2s_compress(
    state: Blake2sState, byte_count: u32, msg: Blake2sInput,
) -&gt; Blake2sState nopanic;</code></pre>

