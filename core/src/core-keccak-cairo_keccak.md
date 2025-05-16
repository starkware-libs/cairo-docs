# cairo_keccak

Computes the Keccak-256 hash of a byte sequence with custom padding.This function allows hashing arbitrary byte sequences by providing the input as 64-bit words in little-endian format and a final partial word.  # Arguments`input` - Array of complete 64-bit words in little-endian format * `last_input_word` - Final partial word (if any) * `last_input_num_bytes` - Number of valid bytes in the final word (0-7)  # ReturnsThe 32-byte Keccak-256 hash as a little-endian `u256`  # PanicsPanics if `last_input_num_bytes` is greater than 7.  # Examples
```cairo
use core::keccak::cairo_keccak;

// Hash "Hello world!" by splitting into 64-bit words in little-endian
let mut input = array![0x6f77206f6c6c6548]; // a full 8-byte word
let hash = cairo_keccak(ref input, 0x21646c72, 4); // 4 bytes of the last word
assert!(hash == 0xabea1f2503529a21734e2077c8b584d7bee3f45550c2d2f12a198ea908e1d0ec);
```

Fully qualified path: `core::keccak::cairo_keccak`

<pre><code class="language-rust">pub fn cairo_keccak(
    ref input: Array&lt;u64&gt;, last_input_word: u64, last_input_num_bytes: usize,
) -&gt; u256</code></pre>

