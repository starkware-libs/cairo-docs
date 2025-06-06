# is_eth_signature_valid

Validates an Ethereum signature against a message hash and Ethereum address.
Similar to `verify_eth_signature` but returns a `Result` instead of panicking.
Also verifies that `r` and `s` components of the signature are in the range `[1, N)`,
where N is the size of the curve.
# Arguments

- `msg_hash` - The 32-byte hash of the message that was signed
- `signature` - The Ethereum signature containing `r`, `s` components and `y_parity`
- `eth_address` - The expected Ethereum address of the signer
# Returns

Returns `Ok(())` if the signature is valid, or `Err(felt252)` containing an error message if
invalid.
# Examples

```cairo
use starknet::eth_address::EthAddress;
use starknet::eth_signature::is_eth_signature_valid;
use starknet::secp256_trait::Signature;

let msg_hash = 0xe888fbb4cf9ae6254f19ba12e6d9af54788f195a6f509ca3e934f78d7a71dd85;
let r = 0x4c8e4fbc1fbb1dece52185e532812c4f7a5f81cf3ee10044320a0d03b62d3e9a;
let s = 0x4ac5e5c0c0e8a4871583cc131f35fb49c2b7f60e6a8b84965830658f08f7410c;
let y_parity = true;
let eth_address: EthAddress = 0x767410c1bb448978bd42b984d7de5970bcaf5c43_u256
    .try_into()
    .unwrap();
assert!(is_eth_signature_valid(msg_hash, Signature { r, s, y_parity }, eth_address).is_ok());
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[eth_signature](./core-starknet-eth_signature.md)::[is_eth_signature_valid](./core-starknet-eth_signature-is_eth_signature_valid.md)

<pre><code class="language-cairo">pub fn is_eth_signature_valid(
    msg_hash: <a href="core-integer-u256.html">u256</a>, signature: <a href="core-starknet-secp256_trait-Signature.html">Signature</a>, eth_address: <a href="core-starknet-eth_address-EthAddress.html">EthAddress</a>,
) -&gt; <a href="core-result-Result.html">Result&lt;(), felt252&gt;</a></code></pre>

