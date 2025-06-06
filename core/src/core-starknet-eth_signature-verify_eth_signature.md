# verify_eth_signature

Asserts that an Ethereum signature is valid for a given message hash and Ethereum address.
Also verifies that the `r` and `s` components of the signature are in the range `[1, N)`,
where N is the size of the curve.
# Arguments

- `msg_hash` - The 32-byte hash of the message that was signed
- `signature` - The Ethereum signature containing `r`, `s` components and `y_parity`
- `eth_address` - The expected Ethereum address of the signer
# Panics

Panics if:
- The signature components are out of range (not in [1, N) where N is the curve order)
- The recovered address doesn't match the provided address
# Examples

```cairo
use starknet::eth_address::EthAddress;
use starknet::eth_signature::verify_eth_signature;
use starknet::secp256_trait::Signature;

let msg_hash = 0xe888fbb4cf9ae6254f19ba12e6d9af54788f195a6f509ca3e934f78d7a71dd85;
let r = 0x4c8e4fbc1fbb1dece52185e532812c4f7a5f81cf3ee10044320a0d03b62d3e9a;
let s = 0x4ac5e5c0c0e8a4871583cc131f35fb49c2b7f60e6a8b84965830658f08f7410c;
let y_parity = true;
let eth_address: EthAddress = 0x767410c1bb448978bd42b984d7de5970bcaf5c43_u256
    .try_into()
    .unwrap();
verify_eth_signature(msg_hash, Signature { r, s, y_parity }, eth_address);
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[eth_signature](./core-starknet-eth_signature.md)::[verify_eth_signature](./core-starknet-eth_signature-verify_eth_signature.md)

<pre><code class="language-cairo">pub fn verify_eth_signature(msg_hash: <a href="core-integer-u256.html">u256</a>, signature: <a href="core-starknet-secp256_trait-Signature.html">Signature</a>, eth_address: <a href="core-starknet-eth_address-EthAddress.html">EthAddress</a>)</code></pre>

