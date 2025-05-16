# Signature

Represents a Secp256{k/r}1 ECDSA signature.This struct holds the components of an ECDSA signature: `r`, `s`, and `y_parity`.

Fully qualified path: `core::starknet::secp256_trait::Signature`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug, PartialEq, Serde, Hash)]
pub struct Signature {
    pub r: u256,
    pub s: u256,
    pub y_parity: bool,
}</code></pre>

## Members

### r

Fully qualified path: `core::starknet::secp256_trait::Signature::r`

<pre><code class="language-rust">pub r: u256</code></pre>


### s

Fully qualified path: `core::starknet::secp256_trait::Signature::s`

<pre><code class="language-rust">pub s: u256</code></pre>


### y_parity

The parity of the y coordinate of the elliptic curve point whose x coordinate is `r`. `y_parity == true` means that the y coordinate is odd. Some places use non boolean `v` instead of `y_parity`. In that case, `signature_from_vrs` should be used.

Fully qualified path: `core::starknet::secp256_trait::Signature::y_parity`

<pre><code class="language-rust">pub y_parity: bool</code></pre>


