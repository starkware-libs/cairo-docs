
[Free functions](./core-starknet-secp256_trait-free_functions.md)
 ---
| | |
|:---|:---|
| [signature_from_vrs](./core-starknet-secp256_trait-signature_from_vrs.md) | Creates an ECDSA signature from the `v` , `r` , and `s`  values. `v`  is the sum of an odd number and the parity of the y coordinate of the ec point whose x coordinate is `r` .[...](./core-starknet-secp256_trait-signature_from_vrs.md) |
| [is_signature_entry_valid](./core-starknet-secp256_trait-is_signature_entry_valid.md) | Checks whether the given `value`  is in the range [ 1, N), where N is the size of the curve. For ECDSA signatures to be secure, both `r`  and `s`  components must be in the range [ 1, N),[...](./core-starknet-secp256_trait-is_signature_entry_valid.md) |
| [is_valid_signature](./core-starknet-secp256_trait-is_valid_signature.md) | Checks whether a signature is valid given a public key point and a message hash.[...](./core-starknet-secp256_trait-is_valid_signature.md) |
| [recover_public_key](./core-starknet-secp256_trait-recover_public_key.md) | Recovers the public key associated with a given signature and message hash. Returns the public key as a point on the curve.[...](./core-starknet-secp256_trait-recover_public_key.md) |
