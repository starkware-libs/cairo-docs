# sha256

Implementation of the SHA-256 cryptographic hash function.
This module provides functions to compute SHA-256 hashes of data.
The input data can be an array of 32-bit words, or a `ByteArray`.
# Examples

```cairo
use core::sha256::compute_sha256_byte_array;

let data = "Hello";
let hash = compute_sha256_byte_array(@data);
assert!(hash == [0x185f8db3, 0x2271fe25, 0xf561a6fc, 0x938b2e26, 0x4306ec30, 0x4eda5180,
0x7d17648, 0x26381969]);
```

Fully qualified path: [core](./core.md)::[sha256](./core-sha256.md)


[Free functions](./core-sha256-free_functions.md)
 ---
| | |
|:---|:---|
| [compute_sha256_u32_array](./core-sha256-compute_sha256_u32_array.md) | Computes the SHA-256 hash of an array of 32-bit words.[...](./core-sha256-compute_sha256_u32_array.md) |
| [compute_sha256_byte_array](./core-sha256-compute_sha256_byte_array.md) | Computes the SHA-256 hash of the input `ByteArray` .[...](./core-sha256-compute_sha256_byte_array.md) |
