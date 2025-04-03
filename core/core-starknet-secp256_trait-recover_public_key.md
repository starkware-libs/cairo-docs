# recover_public_key

Receives a signature and the signed message hash. Returns the public key associated with the signer, represented as a point on the curve.

Fully qualified path: `core::starknet::secp256_trait::recover_public_key`

```rust
pub fn recover_public_key<
    Secp256Point,
    +Drop<Secp256Point>,
    impl Secp256Impl: Secp256Trait<Secp256Point>,
    +Secp256PointTrait<Secp256Point>,
>(
    msg_hash: u256, signature: Signature,
) -> Option<Secp256Point>
```

