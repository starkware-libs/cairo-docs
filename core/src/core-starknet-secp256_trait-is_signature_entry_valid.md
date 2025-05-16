# is_signature_entry_valid

Checks whether the given `value` is in the range [1, N), where N is the size of the curve.For ECDSA signatures to be secure, both `r` and `s` components must be in the range [1, N), where N is the order of the curve. Enforcing this range prevents signature malleability attacks where an attacker could create multiple valid signatures for the same message by adding multiples of N. This function validates that a given value meets this requirement.  # ReturnsReturns `true` if the value is in the valid range [1, N), `false` otherwise.  # Examples
```cairo
use starknet::secp256r1::Secp256r1Point;
use starknet::secp256_trait::is_signature_entry_valid;

assert!(!is_signature_entry_valid::<Secp256r1Point>(0));
```

Fully qualified path: `core::starknet::secp256_trait::is_signature_entry_valid`

<pre><code class="language-rust">pub fn is_signature_entry_valid&lt;
    Secp256Point, +Drop&lt;Secp256Point&gt;, impl Secp256Impl: Secp256Trait&lt;Secp256Point&gt;,
&gt;(
    value: u256,
) -&gt; bool</code></pre>

