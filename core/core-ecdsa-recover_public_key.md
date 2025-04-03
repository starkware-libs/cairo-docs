# recover_public_key

Receives a signature and the signed message hash. Returns the public key associated with the signer.

Fully qualified path: `core::ecdsa::recover_public_key`

```rust
pub fn recover_public_key(
    message_hash: felt252, signature_r: felt252, signature_s: felt252, y_parity: bool,
) -> Option<felt252>
```

