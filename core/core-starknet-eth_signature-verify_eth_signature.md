# verify_eth_signature

Asserts that an Ethereum signature is valid w.r.t. a given Eth address Also verifies that r and s components of the signature are in the range (0, N), where N is the size of the curve.

Fully qualified path: `core::starknet::eth_signature::verify_eth_signature`

```rust
pub fn verify_eth_signature(msg_hash: u256, signature: Signature, eth_address: EthAddress)
```

