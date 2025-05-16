# starknet

Functionalities for interacting with the Starknet network.  # Core ComponentsStorage: The `storage` module defines abstractions on how to interact with Starknet contract storage. - Syscalls: The `syscalls` module contains the extern declarations for all the system calls available in Starknet. - Contract Addresses: The `contract_address` and `eth_address` modules provide types and utilities for working with Starknet contract addresses and Ethereum addresses. - Cryptography: The `secp256k1`, `secp256r1`, `secp256_trait`, and `eth_signature` modules handle various elliptic curve operations. - Execution Info: The `info` module exposes functions for accessing information about the current contract execution, such as the caller address, contract address, block info, and transaction info.

Fully qualified path: `core::starknet`

## Modules

- [storage_access](./core-starknet-storage_access.md)

- [syscalls](./core-starknet-syscalls.md)

- [contract_address](./core-starknet-contract_address.md)

- [secp256_trait](./core-starknet-secp256_trait.md)

- [secp256k1](./core-starknet-secp256k1.md)

- [secp256r1](./core-starknet-secp256r1.md)

- [eth_address](./core-starknet-eth_address.md)

- [eth_signature](./core-starknet-eth_signature.md)

- [class_hash](./core-starknet-class_hash.md)

- [event](./core-starknet-event.md)

- [account](./core-starknet-account.md)

- [storage](./core-starknet-storage.md)

- [testing](./core-starknet-testing.md)

## Constants

- [VALIDATED](./core-starknet-VALIDATED.md)

## Free functions

- [get_block_info](./core-starknet-info-get_block_info.md)

- [get_block_number](./core-starknet-info-get_block_number.md)

- [get_block_timestamp](./core-starknet-info-get_block_timestamp.md)

- [get_caller_address](./core-starknet-info-get_caller_address.md)

- [get_contract_address](./core-starknet-info-get_contract_address.md)

- [get_execution_info](./core-starknet-info-get_execution_info.md)

- [get_tx_info](./core-starknet-info-get_tx_info.md)

## Structs

- [EthAddress](./core-starknet-eth_address-EthAddress.md)

- [ExecutionInfo](./core-starknet-info-v2-ExecutionInfo.md)

- [ResourceBounds](./core-starknet-info-v2-ResourceBounds.md)

- [TxInfo](./core-starknet-info-v2-TxInfo.md)

- [BlockInfo](./core-starknet-info-BlockInfo.md)

## Type aliases

- [SyscallResult](./core-starknet-SyscallResult.md)

## Traits

- [SyscallResultTrait](./core-starknet-SyscallResultTrait.md)

- [Store](./core-starknet-storage_access-Store.md)

- [Event](./core-starknet-event-Event.md)

- [AccountContract](./core-starknet-account-AccountContract.md)

## Extern types

- [System](./core-starknet-System.md)

- [StorageAddress](./core-starknet-storage_access-StorageAddress.md)

- [ContractAddress](./core-starknet-contract_address-ContractAddress.md)

- [ClassHash](./core-starknet-class_hash-ClassHash.md)

## Extern functions

- [contract_address_const](./core-starknet-contract_address-contract_address_const.md)

