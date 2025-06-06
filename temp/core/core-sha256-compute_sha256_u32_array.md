# compute_sha256_u32_array

Computes the SHA-256 hash of an array of 32-bit words.  # Arguments  * `input` - An array of `u32` values to hash * `last_input_word` - The final word when input is not word-aligned * `last_input_num_bytes` - Number of bytes in the last input word (must be less than 4)  # Returns  * The SHA-256 hash of the `input array` + `last_input_word` as big endian  # Examples
```cairo
use core::sha256::compute_sha256_u32_array;

let hash = compute_sha256_u32_array(array![0x68656c6c], 0x6f, 1);
assert!(hash == [0x2cf24dba, 0x5fb0a30e, 0x26e83b2a, 0xc5b9e29e, 0x1b161e5c, 0x1fa7425e,
0x73043362, 0x938b9824]);
```

Fully qualified path: `core::sha256::compute_sha256_u32_array`

```rust
pub fn compute_sha256_u32_array(
    mut input: Array<u32>, last_input_word: u32, last_input_num_bytes: u32,
) -> [u32; 8]
```

