# secp256r1

Functions and constructs related to elliptic curve operations on the secp256r1 curve.
This module provides functionality for performing operations on the NIST P-256 (also known as
secp256r1) elliptic curve. It implements the traits defined in the `secp256_trait` module to
ensure consistent behavior across different secp256 curve implementations.
Curve information:
- Base field: q =
0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
- Scalar field: r =
0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
- a = -3
- b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
- Curve equation: y^2 = x^3 + ax + b

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[secp256r1](./core-starknet-secp256r1.md)


[Extern types](./core-starknet-secp256r1-extern_types.md)
 ---
| | |
|:---|:---|
| [Secp256r1Point](./core-starknet-secp256r1-Secp256r1Point.md) | Represents a point on the secp256r1 elliptic curve.[...](./core-starknet-secp256r1-Secp256r1Point.md) |
