# storage_access

Storage access primitives for Starknet contract storage.This module provides abstractions over the system calls for reading from and writing to Starknet contract storage. It includes traits and implementations for storing various data types efficiently.  # Storage ArchitectureStorage addresses range from `[0, 2^251)` * Base addresses can be combined with offsets, allowing storage of up to 255 values sequentially * Multiple storage domains can be supported, each with its own set of storage space. Currently, only the domain `0` is supported. Values stored in domain `0` are committed to Ethereum as part of the state diffs.  # Core Components[`StorageAddress`](./core-starknet-storage_access-StorageAddress.md): Represents a specific storage location * [`StorageBaseAddress`](./core-starknet-storage_access-StorageBaseAddress.md): Base address that can be combined with offsets * [`Store<T>`](`Store<T>`): Core trait for types that can be stored in contract storage * [`StorePacking<T,P>`](`StorePacking<T,P>`): Trait for efficient packing/unpacking of valuesGenerally, you don't need to implement the [`Store`](./core-starknet-storage_access-Store.md) trait yourself. Most types of the core library, at the exception of collection types, implement the [`Store`](./core-starknet-storage_access-Store.md) trait - and thus, you can derive the [`Store`](./core-starknet-storage_access-Store.md) trait for your own types, as long as they don't contain any collections.

Fully qualified path: `core::starknet::storage_access`

## Traits

- [Store](./core-starknet-storage_access-Store.md)

- [StorePacking](./core-starknet-storage_access-StorePacking.md)

## Extern types

- [StorageAddress](./core-starknet-storage_access-StorageAddress.md)

- [StorageBaseAddress](./core-starknet-storage_access-StorageBaseAddress.md)

## Extern functions

- [storage_base_address_const](./core-starknet-storage_access-storage_base_address_const.md)

- [storage_base_address_from_felt252](./core-starknet-storage_access-storage_base_address_from_felt252.md)

- [storage_address_from_base_and_offset](./core-starknet-storage_access-storage_address_from_base_and_offset.md)

- [storage_address_from_base](./core-starknet-storage_access-storage_address_from_base.md)

