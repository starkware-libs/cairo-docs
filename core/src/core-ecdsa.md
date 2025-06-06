# ecdsa

Elliptic Curve Digital Signature Algorithm (ECDSA) for the STARK curve.
This module provides implementations for ECDSA signature verification and public key recovery
specifically tailored for the STARK curve.
Curve information:
- Curve equation: y² ≡ x³ + α·x + β (mod p)
- α = 1
- β = 0x6f21413efbe40de150e596d72f7a8c5609ad26c15c915c1f4cdfcb99cee9e89
- p = 0x0800000000000011000000000000000000000000000000000000000000000001 = 2^251 + 17 * 2^192 +
1
Generator point:
- x = 0x1ef15c18599971b7beced415a40f0c7deacfd9b0d1819e03d723d8bc943cfca
- y = 0x5668060aa49730b7be4801df46ec62de53ecd11abe43a32873000c36e8dc1f

Fully qualified path: [core](./core.md)::[ecdsa](./core-ecdsa.md)


[Free functions](./core-ecdsa-free_functions.md)
 ---
| | |
|:---|:---|
| [check_ecdsa_signature](./core-ecdsa-check_ecdsa_signature.md) | Verifies an ECDSA signature against a message hash and public key. Note: the verification algorithm implemented by this function slightly deviates from the standard ECDSA.[...](./core-ecdsa-check_ecdsa_signature.md) |
| [recover_public_key](./core-ecdsa-recover_public_key.md) | Recovers the public key from an ECDSA signature and message hash. Given a valid ECDSA signature, the original message hash, and the y-coordinate parity of point[...](./core-ecdsa-recover_public_key.md) |
