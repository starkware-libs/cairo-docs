# Introduction

## What is the Cairo core library?

The Cairo core library provides the foundational building blocks for writing provable programs in Cairo. It offers essential utilities, data structures, mathematical functions, cryptographic tools, and system interactions making it suitable for both onchain and offchain development. Whether you are working on Starknet smart contracts, cryptographic applications, or general-purpose Cairo programs, the core library provides the fundamental tools needed.

you can access modules from the corelib in your program via the core prefix as follows

The core library is available to all  Cairo packages by default, meaning its features are available by simply importing specific modules into your program as follows:

```rust
use core::array::Array;

fn main() {
    let mut arr = Array::new();
    arr.append(42);
}
```

## How to use this documentation?

This documentation serves as a comprehensive reference for all components of the Cairo Core Library. It organizes functionality into modules, constants, functions, types, and traits, allowing developers to explore and understand available features efficiently. It is auto-generated from the core library's codebase using [Scarb](https://docs.swmansion.com/scarb/docs/extensions/documentation-generation.html), so if you find a bug, have a feature request, or want to improve the documentation, simply report an issue or submit a pull request on either [Cairo's](https://github.com/starkware-libs/cairo) or [Scarb's](https://github.com/software-mansion/scarb) GitHub repositories.

If you already know what you are looking for, the fastest way to find it is to use the search bar at the top of the page. Otherwise, you can take [a quick tour of the documentation](#a-quick-tour-of-the-documentation) and start clicking on anything the seems interesting. If this is your first time, we recommend starting with browsing the library's modules and experimenting with their functionality in your Cairo programs.

Happy coding! 𓅃

## A quick tour of the documentation

This documentation is structured into the following sections:

- [Modules](./modules.md) – The main building blocks of the library
This section includes all standard modules, each serving a distinct purpose:

    - Core Utilities:
        - `core` – The base module with essential utilities
        - `traits` – Common behavior definitions used across multiple types
        - `boolean` – Boolean logic operations
        - `array` – Dynamic data structures for storing and managing sequences of values
        - `dict` – Key-value storage structures
        - `option` – Represents optional values
        - `result` – Used for error handling

    - Numerical and Mathematical Modules:
        - `integer` – Fixed-size integer operations (`u8`, `u16`, `u32`, `u64`, etc.)
        - `math` – Core mathematical functions
        - `ops` – Arithmetic and logical operators
        - `num` – Numeric utilities and traits
        - `cmp` – Comparisons and ordering

    - Cryptography and Hashing:
        - `hash` – Generic hash utilities.
        - `poseidon`, `pedersen`, `keccak`, `sha256` – Cryptographic hash functions
        - `ecdsa` – Signature verification and elliptic curve cryptography

    - Starknet-Specific Modules:
        - `starknet` – Essential utilities for writing smart contracts
        - `syscalls` – Low-level Starknet system interactions
        - `storage` – On-chain storage management
        - `event` – Emitting events for contract execution tracking
        - `contract_address` – Starknet contract address utilities
        - `account` – Account contract functionality

    - Other Utilities:
        - `debug` – Debugging tools
        - `fmt` – String formatting utilities
        - `serde` – Serialization and deserialization
        - `metaprogramming` – Advanced compile-time utilities
        - `zeroable` – Zero-initialized types

- Constants – Predefined values for cryptographic and mathematical operations, , such as:
    - `stark_curve::ALPHA, BETA, ORDER` – Constants for Stark curve operations
    - `starknet::VALIDATED` – The expected return value of a Starknet account's `__validate__` function in case of success

- Free Functions – Globally accessible functions that don’t belong to a specific trait, such as:
    - `panic_with_felt252` – Triggers a panic with a given value
    - `get_tx_info` – Returns the transaction info (hash, signature, etc.) for the current transaction

- Structs – Data structures used throughout Cairo programs, such as:
    - `Span<T>` – A lightweight view over a contiguous memory block
    - `Range<T>` – Represents a range of values
    - `BlockInfo`, `TxInfo`, `ExecutionInfo` – Used for retrieving Starknet execution details
    - `EventEmitter` – Helps in emitting events from contracts

- Enums – Enumerations for handling multiple possible values, such as:
    - `Option<T>` – Represents either `Some(value)` or None
    - `Result<T, E>` – Represents either `Ok(value)` or `Err(error)`
    - `PanicResult` – Handles different types of panics in execution.

- Type Aliases – Shorthand for commonly used types, such as:
    - `usize` – Represents an unsigned integer type used for indexing
    - `SyscallResult<T>` – A standardized way of handling syscall return values
    - `NonZeroEcPoint` – Ensures that an elliptic curve point is non-zero

- Traits – Shared behavior implementations for different types, such as:
    - `PartialEq`, `PartialOrd` – Used for comparisons
    - `Iterator`, `IntoIterator` – Traits for iterating over collections
    - `Serialize`, `Deserialize` – Serialization and deserialization behaviors

- Impls – Concrete implementations of traits for various types, such as:
    - `CircuitElementDrop`, `CircuitElementCopy` – Implementations for circuit computations
    - `SpanIndex` – Allows indexing into `Span<T>`
    - `PedersenImpl`, `PoseidonImpl` – Implementations for cryptographic hashing

- Extern Types – Sierra types that are usable in high-level Cairo, such as:
    - `Array<T>` – A collection of elements of the same type continuous in memory.
    - `Box<T>` – A wrapper that enables moving the type around of cheaply
    - `bytes31<T>` – Represents a 31-byte fixed-size byte type.

- Extern Functions – Sierra libfuncs that are usable in high-level Cairo, such as:
    - `hades_permutation` – Hades permutation for triplets of `felt252`
    - `felt252_div` – Division operation for `felt252`
    - `storage_read_syscall`, `storage_write_syscall` – Direct Starknet storage interactions