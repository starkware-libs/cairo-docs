
[Free functions](./core-starknet-eth_signature-free_functions.md)
 ---
| | |
|:---|:---|
| [verify_eth_signature](./core-starknet-eth_signature-verify_eth_signature.md) | Asserts that an Ethereum signature is valid for a given message hash and Ethereum address. Also verifies that the `r`  and `s`  components of the signature are in the range `[1, N)` ,[...](./core-starknet-eth_signature-verify_eth_signature.md) |
| [is_eth_signature_valid](./core-starknet-eth_signature-is_eth_signature_valid.md) | Validates an Ethereum signature against a message hash and Ethereum address. Similar to `verify_eth_signature`  but returns a `Result`  instead of panicking. Also verifies that `r`  and `s`[...](./core-starknet-eth_signature-is_eth_signature_valid.md) |
| [public_key_point_to_eth_address](./core-starknet-eth_signature-public_key_point_to_eth_address.md) | Converts a public key point to its corresponding Ethereum address. The Ethereum address is calculated by taking the Keccak-256 hash of the public key coordinates[...](./core-starknet-eth_signature-public_key_point_to_eth_address.md) |
