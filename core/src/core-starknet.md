# starknet

Functionalities for interacting with the Starknet network.
# Core Components

- Storage: The `storage` module defines abstractions on how to interact with Starknet
contract storage.
- Syscalls: The `syscalls` module contains the extern declarations for all the system calls
available in Starknet.
- Contract Addresses: The `contract_address` and `eth_address` modules provide types and
utilities for working with Starknet contract addresses and Ethereum addresses.
- Cryptography: The `secp256k1`, `secp256r1`, `secp256_trait`, and `eth_signature` modules
handle various elliptic curve operations.
- Execution Info: The `info` module exposes functions for accessing information about the
current contract execution, such as the caller address, contract address, block info, and
transaction info.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)


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

[Constants](./core-starknet-constants.md)
 ---
| | |
|:---|:---|
| [VALIDATED](./core-starknet-VALIDATED.md) | The expected return value of the `__validate__`  function in account contracts. This constant is used to indicate that a transaction validation was successful.[...](./core-starknet-VALIDATED.md) |

[Type aliases](./core-starknet-type_aliases.md)
 ---
| | |
|:---|:---|
| [SyscallResult](./core-starknet-SyscallResult.md) | The `Result`  type for a syscall.[...](./core-starknet-SyscallResult.md) |

[Traits](./core-starknet-traits.md)
 ---
| | |
|:---|:---|
| [SyscallResultTrait](./core-starknet-SyscallResultTrait.md) | Trait for handling syscall results.[...](./core-starknet-SyscallResultTrait.md) |

[Extern types](./core-starknet-extern_types.md)
 ---
| | |
|:---|:---|
| [System](./core-starknet-System.md) | [...](./core-starknet-System.md) |
## Re-exports

 - ### Free functions

| | |
|:---|:---|
| [get_block_info](./core-starknet-info-get_block_info.md) | Returns the block information for the current block.[...](./core-starknet-info-get_block_info.md) |
| [get_block_number](./core-starknet-info-get_block_number.md) | Returns the number of the current block.[...](./core-starknet-info-get_block_number.md) |
| [get_block_timestamp](./core-starknet-info-get_block_timestamp.md) | Returns the timestamp of the current block.[...](./core-starknet-info-get_block_timestamp.md) |
| [get_caller_address](./core-starknet-info-get_caller_address.md) | Returns the address of the caller contract. Returns `0`  if there is no caller—for example, when a transaction begins execution inside an account contract. Note: This function returns the direct[...](./core-starknet-info-get_caller_address.md) |
| [get_contract_address](./core-starknet-info-get_contract_address.md) | Returns the address of the contract being executed.[...](./core-starknet-info-get_contract_address.md) |
| [get_execution_info](./core-starknet-info-get_execution_info.md) | Returns the execution info for the current execution.[...](./core-starknet-info-get_execution_info.md) |
| [get_tx_info](./core-starknet-info-get_tx_info.md) | Returns the transaction information for the current transaction.[...](./core-starknet-info-get_tx_info.md) |

<br>


 - ### Structs

| | |
|:---|:---|
| [EthAddress](./core-starknet-eth_address-EthAddress.md) | An Ethereum address, 20 bytes in length.[...](./core-starknet-eth_address-EthAddress.md) |
| [ExecutionInfo](./core-starknet-info-v2-ExecutionInfo.md) | The same as `ExecutionInfo` , but with the `TxInfo`  field replaced with `v2::TxInfo` .[...](./core-starknet-info-v2-ExecutionInfo.md) |
| [ResourceBounds](./core-starknet-info-v2-ResourceBounds.md) | V3 transactions resources used for enabling the fee market.[...](./core-starknet-info-v2-ResourceBounds.md) |
| [TxInfo](./core-starknet-info-v2-TxInfo.md) | Extended information about the current transaction.[...](./core-starknet-info-v2-TxInfo.md) |
| [BlockInfo](./core-starknet-info-BlockInfo.md) | Information about the current block.[...](./core-starknet-info-BlockInfo.md) |

<br>


 - ### Traits

| | |
|:---|:---|
| [Store](./core-starknet-storage_access-Store.md) | Trait for types that can be stored in Starknet contract storage. The `Store`  trait enables types to be stored in and retrieved from Starknet's contract storage. Cairo implements `Store`[...](./core-starknet-storage_access-Store.md) |
| [Event](./core-starknet-event-Event.md) | A trait for handling serialization and deserialization of events. Events in Starknet are stored in transaction receipts as a combination of keys and data fields.[...](./core-starknet-event-Event.md) |
| [AccountContract](./core-starknet-account-AccountContract.md) | A trait for account contracts that support class declarations (only `__validate__`  and `__execute__`  are mandatory for an account). This trait assumes that the calldata for invoke transactions is[...](./core-starknet-account-AccountContract.md) |

<br>


 - ### Extern types

| | |
|:---|:---|
| [StorageAddress](./core-starknet-storage_access-StorageAddress.md) | Represents the address of a storage value in a Starknet contract. The value range of this type is `[0, 2**251)` .[...](./core-starknet-storage_access-StorageAddress.md) |
| [ContractAddress](./core-starknet-contract_address-ContractAddress.md) | Represents a Starknet contract address. The value range of this type is `[0, 2**251)` .[...](./core-starknet-contract_address-ContractAddress.md) |
| [ClassHash](./core-starknet-class_hash-ClassHash.md) | Represents a Starknet contract class hash. The value range of this type is `[0, 2**251)` .[...](./core-starknet-class_hash-ClassHash.md) |

<br>


 - ### Extern functions

| | |
|:---|:---|
| [contract_address_const](./core-starknet-contract_address-contract_address_const.md) | Returns a `ContractAddress`  given a `felt252`  value.[...](./core-starknet-contract_address-contract_address_const.md) |

<br>

