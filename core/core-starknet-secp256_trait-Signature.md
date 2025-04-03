# Signature

Secp256{k/r}1 ECDSA signature.

Fully qualified path: `core::starknet::secp256_trait::Signature`

```rust
#[derive(Copy, Drop, Debug, PartialEq, Serde, Hash)]
pub struct Signature {
    pub r: u256,
    pub s: u256,
    pub y_parity: bool,
}
```

