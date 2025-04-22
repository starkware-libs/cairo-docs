# is_eth_signature_valid

Asserts that an Ethereum signature is valid w.r.t. a given Eth address Also verifies that r and s components of the signature are in the range (0, N), where N is the size of the curve. Returns a Result with an error string if the signature is invalid.

Fully qualified path: `core::starknet::eth_signature::is_eth_signature_valid`

```rust
pub fn is_eth_signature_valid(
    msg_hash: u256, signature: Signature, eth_address: EthAddress,
) -> Result<(), felt252>
```

