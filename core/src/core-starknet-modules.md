
[Modules](./core-starknet-modules.md)
 ---
| | |
|:---|:---|
| [storage_access](./core-starknet-storage_access.md) | Storage access primitives for Starknet contract storage. This module provides abstractions over the system calls for reading from and writing to Starknet[...](./core-starknet-storage_access.md) |
| [syscalls](./core-starknet-syscalls.md) | Utilities for interacting with the Starknet OS. Writing smart contracts requires various associated operations, such as calling another contract[...](./core-starknet-syscalls.md) |
| [contract_address](./core-starknet-contract_address.md) | The `ContractAddress`  type represents a Starknet contract address, with a value range of `[0, 2**251)` . A variable of type `ContractAddress`  can be created from a `felt252`  value using the[...](./core-starknet-contract_address.md) |
| [secp256_trait](./core-starknet-secp256_trait.md) | Elliptic Curve Digital Signature Algorithm (ECDSA) for Secp256k1 and Secp256r1 curves. This module provides traits and functions for working with ECDSA signatures[...](./core-starknet-secp256_trait.md) |
| [secp256k1](./core-starknet-secp256k1.md) | Functions and constructs related to elliptic curve operations on the secp256k1 curve. This module provides functionality for performing operations on the secp256k1 elliptic curve,[...](./core-starknet-secp256k1.md) |
| [secp256r1](./core-starknet-secp256r1.md) | Functions and constructs related to elliptic curve operations on the secp256r1 curve. This module provides functionality for performing operations on the NIST P-256 (also known as[...](./core-starknet-secp256r1.md) |
| [eth_address](./core-starknet-eth_address.md) | Ethereum address type for working with Ethereum primitives. This module provides the [`EthAddress`](./core-starknet-eth_address-EthAddress.md)  type, which is used when interacting with Ethereum[...](./core-starknet-eth_address.md) |
| [eth_signature](./core-starknet-eth_signature.md) | Utilities for Ethereum signature verification and address recovery. This module provides functionality for working with Ethereum signatures.[...](./core-starknet-eth_signature.md) |
| [class_hash](./core-starknet-class_hash.md) | The `ClassHash`  type represents a Starknet contract class hash, with a value range of `[0, 2**251)` . A variable of type `ClassHash`  can be created from a `felt252`  value using the[...](./core-starknet-class_hash.md) |
| [event](./core-starknet-event.md) | Event handling traits for Starknet smart contracts. This module provides traits for serializing, deserializing and emitting events on Starknet. The [`Event`](./core-starknet-event-Event.md)[...](./core-starknet-event.md) |
| [account](./core-starknet-account.md) | Account module defining the `Call`  struct and the [`AccountContract`](./core-starknet-account-AccountContract.md)  trait. The `Call`[...](./core-starknet-account.md) |
| [storage](./core-starknet-storage.md) | Storage-related types and traits for Cairo contracts. This module implements the storage system for Starknet contracts, providing high-level[...](./core-starknet-storage.md) |
| [testing](./core-starknet-testing.md) | Testing utilities for Starknet contracts. This module provides functions for testing Starknet contracts. The functions[...](./core-starknet-testing.md) |
| [info](./core-starknet-info.md) | Information about the Starknet execution environment. This module provides access to runtime information about the current transaction,[...](./core-starknet-info.md) |
