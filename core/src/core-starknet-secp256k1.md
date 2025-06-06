# secp256k1

Functions and constructs related to elliptic curve operations on the secp256k1 curve.
This module provides functionality for performing operations on the secp256k1 elliptic curve,
commonly used in cryptographic applications such as Bitcoin and Ethereum.
It implements the traits defined in the `secp256_trait` module to ensure consistent behavior
across different secp256 curve implementations.
Curve information:
- Base field: q =
0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
- Scalar field: r =
0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
- Curve equation: y^2 = x^3 + 7

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[secp256k1](./core-starknet-secp256k1.md)


[Extern types](./core-starknet-secp256k1-extern_types.md)
 ---
| | |
|:---|:---|
| [Secp256k1Point](./core-starknet-secp256k1-Secp256k1Point.md) | A point on the secp256k1 curve.[...](./core-starknet-secp256k1-Secp256k1Point.md) |
