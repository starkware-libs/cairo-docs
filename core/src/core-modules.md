
[Modules](./core-modules.md)
 ---
| | |
|:---|:---|
| [traits](./core-traits.md) | Core traits for various operations. This module provides a collection of essential traits that define common behavior patterns for Cairo types.[...](./core-traits.md) |
| [boolean](./core-boolean.md) | Boolean operations. The `bool`  type is a primitive type in Cairo representing a boolean value that can be either `true`  or `false`[...](./core-boolean.md) |
| [circuit](./core-circuit.md) | Efficient modular arithmetic computations using arithmetic circuits. This module provides a type-safe way to perform modular arithmetic operations using[...](./core-circuit.md) |
| [blake](./core-blake.md) | [...](./core-blake.md) |
| [box](./core-box.md) | `Box<T>`  is a smart pointer that allows for:[...](./core-box.md) |
| [nullable](./core-nullable.md) | A wrapper type for handling optional values. `Nullable<T>`  is a wrapper type that can either contain a value stored in a `Box<T>`[...](./core-nullable.md) |
| [array](./core-array.md) | A contiguous collection of elements of the same type in memory, written `Array<T>` . Arrays have O (1) indexing, O (1) push and O (1) pop (from the front).[...](./core-array.md) |
| [dict](./core-dict.md) | A dictionary-like data structure that maps `felt252`  keys to values of any type. The `Felt252Dict`  provides efficient key-value storage with operations for inserting,[...](./core-dict.md) |
| [result](./core-result.md) | Error handling with the `Result`  type. [`Result`](./core-result-Result.md)  is the type used for returning and propagating errors. It is an enum with the variants, `Ok(T)` , representing[...](./core-result.md) |
| [option](./core-option.md) | Optional values. The [`Option`](./core-option-Option.md)  type represents an optional value: every [`Option`](./core-option-Option.md)  is either [`Some`](./core-option.md#some)  and[...](./core-option.md) |
| [clone](./core-clone.md) | The `Clone`  trait provides the ability to duplicate instances of types that cannot be 'implicitly copied'. In Cairo, some simple types are "implicitly copyable": when you assign them or pass them as[...](./core-clone.md) |
| [ec](./core-ec.md) | Functions and constructs related to elliptic curve operations on the STARK curve. This module provides implementations for various elliptic curve operations tailored for the STARK curve.[...](./core-ec.md) |
| [ecdsa](./core-ecdsa.md) | Elliptic Curve Digital Signature Algorithm (ECDSA) for the STARK curve. This module provides implementations for ECDSA signature verification and public key recovery[...](./core-ecdsa.md) |
| [integer](./core-integer.md) | Integer types and operations. This module provides the built-in integer types and their associated operations.[...](./core-integer.md) |
| [cmp](./core-cmp.md) | Utilities for comparing and ordering values. This module contains functions that rely on the `PartialOrd`  trait for comparing values.[...](./core-cmp.md) |
| [gas](./core-gas.md) | Utilities for handling gas in Cairo code.[...](./core-gas.md) |
| [math](./core-math.md) | Mathematical operations and utilities. Provides extended GCD, modular inverse, and modular arithmetic operations.[...](./core-math.md) |
| [num](./core-num.md) | [...](./core-num.md) |
| [ops](./core-ops.md) | Overloadable operators. Implementing these traits allows you to overload certain operators. Note: Other overloadable operators are also defined in the [`core::traits`](./core-traits.md)  module.[...](./core-ops.md) |
| [panics](./core-panics.md) | Core panic mechanism. This module provides the core panic functionality used for error handling in Cairo. It defines the basic types and functions used to trigger and manage panics, which[...](./core-panics.md) |
| [hash](./core-hash.md) | Generic hashing support. This module provides a hash state abstraction that can be updated with values and finalized to[...](./core-hash.md) |
| [keccak](./core-keccak.md) | Keccak-256 cryptographic hash function implementation.[...](./core-keccak.md) |
| [pedersen](./core-pedersen.md) | Pedersen hash related traits implementations. This module provides an implementation of the Pedersen hash function, which is a collision-resistant cryptographic hash function. The `HashState`[...](./core-pedersen.md) |
| [qm31](./core-qm31.md) | Definition for the `qm31`  type. Only available for local proofs. The implementations defined in this module can be accessed by using the traits directly.[...](./core-qm31.md) |
| [serde](./core-serde.md) | Serialization and deserialization of data structures. This module provides traits and implementations for converting Cairo types into a sequence of `felt252`[...](./core-serde.md) |
| [sha256](./core-sha256.md) | Implementation of the SHA-256 cryptographic hash function. This module provides functions to compute SHA-256 hashes of data. The input data can be an array of 32-bit words, or a `ByteArray` .[...](./core-sha256.md) |
| [poseidon](./core-poseidon.md) | Poseidon hash related traits implementations and functions. This module provides cryptographic hash functions based on the Poseidon permutation.[...](./core-poseidon.md) |
| [debug](./core-debug.md) | Utilities related to printing of values at runtime. The recommended way of printing values is by using the `Display`  and `Debug`  traits available in the [`fmt`](./core-fmt.md)[...](./core-debug.md) |
| [fmt](./core-fmt.md) | Functionality for formatting values. The main components of this module are:[...](./core-fmt.md) |
| [starknet](./core-starknet.md) | Functionalities for interacting with the Starknet network.[...](./core-starknet.md) |
| [internal](./core-internal.md) | [...](./core-internal.md) |
| [zeroable](./core-zeroable.md) | Types and traits for handling non-zero values and zero checking operations. This module provides the [`NonZero`](./core-zeroable-NonZero.md)  wrapper type which guarantees that a value is never zero.[...](./core-zeroable.md) |
| [bytes_31](./core-bytes_31.md) | Definitions and utilities for the `bytes31`  type. The `bytes31`  type is a compact, indexable 31-byte type.[...](./core-bytes_31.md) |
| [byte_array](./core-byte_array.md) | `ByteArray`  is designed to handle large sequences of bytes with operations like appending, concatenation, and accessing individual bytes. It uses a structure that combines an `Array`  of `bytes31`[...](./core-byte_array.md) |
| [string](./core-string.md) | [...](./core-string.md) |
| [iter](./core-iter.md) | Composable external iteration. If you've found yourself with a collection of some kind, and needed to perform an operation on the elements of said collection, you'll quickly run[...](./core-iter.md) |
| [metaprogramming](./core-metaprogramming.md) | Metaprogramming utilities.[...](./core-metaprogramming.md) |
| [testing](./core-testing.md) | Measurement of gas consumption for testing purpose. This module provides the `get_available_gas`  function, useful for asserting the amount of gas consumed by a particular operation or function call.[...](./core-testing.md) |
| [to_byte_array](./core-to_byte_array.md) | ASCII representation of numeric types for `ByteArray`  manipulation. This module enables conversion of numeric values into their ASCII string representation,[...](./core-to_byte_array.md) |
