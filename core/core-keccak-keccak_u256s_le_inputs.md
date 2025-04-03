# keccak_u256s_le_inputs

Computes the keccak256 of multiple u256 values. The input values are interpreted as little-endian. The 32-byte result is represented as a little-endian u256.

Fully qualified path: `core::keccak::keccak_u256s_le_inputs`

```rust
pub fn keccak_u256s_le_inputs(mut input: Span<u256>) -> u256
```

