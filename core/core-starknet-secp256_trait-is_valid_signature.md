# is_valid_signature

Fully qualified path: `core::starknet::secp256_trait::is_valid_signature`

```rust
pub fn is_valid_signature<
    Secp256Point,
    +Drop<Secp256Point>,
    impl Secp256Impl: Secp256Trait<Secp256Point>,
    +Secp256PointTrait<Secp256Point>,
>(
    msg_hash: u256, r: u256, s: u256, public_key: Secp256Point,
) -> bool
```

