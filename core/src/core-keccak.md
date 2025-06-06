# keccak

Keccak-256 cryptographic hash function implementation.
# Main Functions

- `keccak_u256s_le_inputs` - Hash multiple `u256` values in little-endian format
- `keccak_u256s_be_inputs` - Hash multiple `u256` values in big-endian format
- `cairo_keccak` - Hash u64 words with a final partial word. Closest to the syscall input.
- `compute_keccak_byte_array` - Hash a `ByteArray` directly
# Examples

```cairo
use core::keccak::*;

// Hash u256 values
let input = array![1_u256, 2_u256].span();
assert!(keccak_u256s_le_inputs(input) ==
0x234a9e12e9b063b60f7e3289ee9b86a731de8e7e41bd4987f10982d6a753444d);
assert!(keccak_u256s_be_inputs(input) ==
0xe0c2a7d2cc99d544061ac0ccbb083ac8976e54eed878fb1854dfe7b6ce7b0be9);

// Hash a `Bytearray`
let text: ByteArray = "Hello, Keccak!";
assert!(compute_keccak_byte_array(@text) ==
0x85c9aab73219c1e95c5b5966a4ecc8db4418c3500072a830cfb5a2d13d2c2249);
```

Fully qualified path: [core](./core.md)::[keccak](./core-keccak.md)


[Free functions](./core-keccak-free_functions.md)
 ---
| | |
|:---|:---|
| [keccak_u256s_le_inputs](./core-keccak-keccak_u256s_le_inputs.md) | Computes the Keccak-256 hash of multiple `u256`  values in little-endian format.[...](./core-keccak-keccak_u256s_le_inputs.md) |
| [keccak_u256s_be_inputs](./core-keccak-keccak_u256s_be_inputs.md) | Computes the Keccak-256 hash of multiple `u256`  values in big-endian format.[...](./core-keccak-keccak_u256s_be_inputs.md) |
| [cairo_keccak](./core-keccak-cairo_keccak.md) | Computes the Keccak-256 hash of a byte sequence with custom padding. This function allows hashing arbitrary byte sequences by providing the input as[...](./core-keccak-cairo_keccak.md) |
| [compute_keccak_byte_array](./core-keccak-compute_keccak_byte_array.md) | Computes the Keccak-256 hash of a `ByteArray` .[...](./core-keccak-compute_keccak_byte_array.md) |
