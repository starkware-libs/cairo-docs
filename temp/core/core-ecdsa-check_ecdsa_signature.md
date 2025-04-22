# check_ecdsa_signature

Checks if (`signature_r`, `signature_s`) is a valid ECDSA signature for the given `public_key` on the given `message`.  Note: the verification algorithm implemented by this function slightly deviates from the standard ECDSA. While this does not allow to create valid signatures if one does not possess the private key, it means that the signature algorithm used should be modified accordingly. Namely, it should check that `r, s < stark_curve::ORDER`.  Arguments: * `message_hash` - the signed message. * `public_key` - the public key corresponding to the key with which the message was signed. * `signature_r` - the `r` component of the ECDSA signature. * `signature_s` - the `s` component of the ECDSA signature.  Returns:   `true` if the signature is valid and `false` otherwise.

Fully qualified path: `core::ecdsa::check_ecdsa_signature`

```rust
pub fn check_ecdsa_signature(
    message_hash: felt252, public_key: felt252, signature_r: felt252, signature_s: felt252,
) -> bool
```

