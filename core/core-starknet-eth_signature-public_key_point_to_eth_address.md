# public_key_point_to_eth_address

Converts a public key point to the corresponding Ethereum address.

Fully qualified path: `core::starknet::eth_signature::public_key_point_to_eth_address`

```rust
pub fn public_key_point_to_eth_address<
    Secp256Point,
    +Drop<Secp256Point>,
    +Secp256Trait<Secp256Point>,
    +Secp256PointTrait<Secp256Point>,
>(
    public_key_point: Secp256Point,
) -> EthAddress
```

