# compute_keccak_byte_array

Computes the Keccak-256 hash of a `ByteArray`.  # Arguments`arr` - The input bytes to hash  # ReturnsThe 32-byte Keccak-256 hash as a little-endian `u256`  # Examples
```cairo
use core::keccak::compute_keccak_byte_array;

let text: ByteArray = "Hello world!";
let hash = compute_keccak_byte_array(@text);
assert!(hash == 0xabea1f2503529a21734e2077c8b584d7bee3f45550c2d2f12a198ea908e1d0ec);
```

Fully qualified path: `core::keccak::compute_keccak_byte_array`

<pre><code class="language-rust">pub fn compute_keccak_byte_array(arr: @ByteArray) -&gt; u256</code></pre>

