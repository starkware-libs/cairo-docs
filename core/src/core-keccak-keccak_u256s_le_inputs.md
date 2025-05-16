# keccak_u256s_le_inputs

Computes the Keccak-256 hash of multiple `u256` values in little-endian format.  # Arguments`input` - A span of little-endian `u256` values to be hashed  # ReturnsThe 32-byte Keccak-256 hash as a little-endian `u256`  # Examples
```cairo
use core::keccak::keccak_u256s_le_inputs;

let input: Span<u256> = array![0, 1, 2].span();
assert!(keccak_u256s_le_inputs(input) ==
0xf005473605efc7d8ff67d9f23fe2e4a4f23454c12b49b38822ed362e0a92a0a6);
```

Fully qualified path: `core::keccak::keccak_u256s_le_inputs`

<pre><code class="language-rust">pub fn keccak_u256s_le_inputs(mut input: Span&lt;u256&gt;) -&gt; u256</code></pre>

