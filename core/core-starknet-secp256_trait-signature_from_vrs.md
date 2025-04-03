# signature_from_vrs

Creates an ECDSA signature from the `v`, `r` and `s` values. `v` is the sum of an odd number and the parity of the y coordinate of the ec point whose x coordinate is `r`. See https://eips.ethereum.org/EIPS/eip-155 for more details.

Fully qualified path: `core::starknet::secp256_trait::signature_from_vrs`

```rust
pub fn signature_from_vrs(v: u32, r: u256, s: u256) -> Signature
```

