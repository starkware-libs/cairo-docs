# sha256

Implementation of the SHA-256 cryptographic hash function.  This module provides functions to compute SHA-256 hashes of data. The input data can be an array of 32-bit words, or a `ByteArray`.  # Examples
```cairo
use core::sha256::compute_sha256_byte_array;

let data = "Hello";
let hash = compute_sha256_byte_array(@data);
assert!(hash == [0x185f8db3, 0x2271fe25, 0xf561a6fc, 0x938b2e26, 0x4306ec30, 0x4eda5180,
0x7d17648, 0x26381969]);
```

Fully qualified path: `core::sha256`

## Free functions

- [compute_sha256_u32_array](./core-sha256-compute_sha256_u32_array.md)

- [compute_sha256_byte_array](./core-sha256-compute_sha256_byte_array.md)

## Extern types

- [Sha256StateHandle](./core-sha256-Sha256StateHandle.md)

