# signature_from_vrs

Creates an ECDSA signature from the `v`, `r`, and `s` values.`v` is the sum of an odd number and the parity of the y coordinate of the ec point whose x coordinate is `r`.See https://eips.ethereum.org/EIPS/eip-155 for more details.  # Examples
```cairo
use starknet::secp256_trait::signature_from_vrs;

let signature = signature_from_vrs(0,
0xa73bd4903f0ce3b639bbbf6e8e80d16931ff4bcf5993d58468e8fb19086e8cac,
0x36dbcd03009df8c59286b162af3bd7fcc0450c9aa81be5d10d312af6c66b1d60);
```

Fully qualified path: `core::starknet::secp256_trait::signature_from_vrs`

<pre><code class="language-rust">pub fn signature_from_vrs(v: u32, r: u256, s: u256) -&gt; Signature</code></pre>

