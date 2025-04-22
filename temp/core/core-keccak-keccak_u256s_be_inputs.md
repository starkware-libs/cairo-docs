# keccak_u256s_be_inputs

Computes the keccak256 of multiple u256 values. The input values are interpreted as big-endian. The 32-byte result is represented as a little-endian u256.

Fully qualified path: `core::keccak::keccak_u256s_be_inputs`

```rust
pub fn keccak_u256s_be_inputs(mut input: Span<u256>) -> u256
```

