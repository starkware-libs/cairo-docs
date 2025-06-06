# secp256_trait

Elliptic Curve Digital Signature Algorithm (ECDSA) for Secp256k1 and Secp256r1 curves.
This module provides traits and functions for working with ECDSA signatures
on the Secp256k1 and the Secp256r1 curves. It includes utilities for creating
and validating signatures, as well as recovering public keys from signatures.
# Examples

```cairo
use starknet::SyscallResultTrait;```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[secp256_trait](./core-starknet-secp256_trait.md)


[Free functions](./core-starknet-secp256_trait-free_functions.md)
 ---
| | |
|:---|:---|
| [signature_from_vrs](./core-starknet-secp256_trait-signature_from_vrs.md) | Creates an ECDSA signature from the `v` , `r` , and `s`  values. `v`  is the sum of an odd number and the parity of the y coordinate of the ec point whose x coordinate is `r` .[...](./core-starknet-secp256_trait-signature_from_vrs.md) |
| [is_signature_entry_valid](./core-starknet-secp256_trait-is_signature_entry_valid.md) | Checks whether the given `value`  is in the range [ 1, N), where N is the size of the curve. For ECDSA signatures to be secure, both `r`  and `s`  components must be in the range [ 1, N),[...](./core-starknet-secp256_trait-is_signature_entry_valid.md) |
| [is_valid_signature](./core-starknet-secp256_trait-is_valid_signature.md) | Checks whether a signature is valid given a public key point and a message hash.[...](./core-starknet-secp256_trait-is_valid_signature.md) |
| [recover_public_key](./core-starknet-secp256_trait-recover_public_key.md) | Recovers the public key associated with a given signature and message hash. Returns the public key as a point on the curve.[...](./core-starknet-secp256_trait-recover_public_key.md) |

[Structs](./core-starknet-secp256_trait-structs.md)
 ---
| | |
|:---|:---|
| [Signature](./core-starknet-secp256_trait-Signature.md) | Represents a Secp256{k/r}1 ECDSA signature. This struct holds the components of an ECDSA signature: `r` , `s` , and `y_parity` .[...](./core-starknet-secp256_trait-Signature.md) |

[Traits](./core-starknet-secp256_trait-traits.md)
 ---
| | |
|:---|:---|
| [Secp256Trait](./core-starknet-secp256_trait-Secp256Trait.md) | A trait for interacting with Secp256{k/r}1 curves. Provides operations needed to work with Secp256k1 and Secp256r1 elliptic curves.[...](./core-starknet-secp256_trait-Secp256Trait.md) |
| [Secp256PointTrait](./core-starknet-secp256_trait-Secp256PointTrait.md) | A trait for performing operations on Secp256{k/r}1 curve points. Provides operations needed for elliptic curve cryptography, including point addition and scalar multiplication.[...](./core-starknet-secp256_trait-Secp256PointTrait.md) |
