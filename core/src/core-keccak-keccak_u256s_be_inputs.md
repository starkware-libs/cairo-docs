# keccak_u256s_be_inputs

Computes the Keccak-256 hash of multiple `u256` values in big-endian format.  # Arguments`input` - A span of big-endian `u256` values to be hashed  # ReturnsThe 32-byte Keccak-256 hash as a little-endian `u256`  # Examples
```cairo
use core::keccak::keccak_u256s_be_inputs;

let input = array![0x1234_u256, 0x5678_u256].span();
let hash = assert!(keccak_u256s_be_inputs(input) ==
0xfa31cb2326ed629f79d2da5beb78e2bd8ac7a1b8b86cae09eeb6a89a908b12a);
```

Fully qualified path: `core::keccak::keccak_u256s_be_inputs`

<pre><code class="language-rust">pub fn keccak_u256s_be_inputs(mut input: Span&lt;u256&gt;) -&gt; u256</code></pre>

