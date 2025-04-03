# is_signature_entry_valid

Checks whether `value` is in the range [1, N), where N is the size of the curve.

Fully qualified path: `core::starknet::secp256_trait::is_signature_entry_valid`

```rust
pub fn is_signature_entry_valid<
    Secp256Point, +Drop<Secp256Point>, impl Secp256Impl: Secp256Trait<Secp256Point>,
>(
    value: u256,
) -> bool
```

