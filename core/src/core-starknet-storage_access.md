# storage_access

Storage access primitives for Starknet contract storage.
This module provides abstractions over the system calls for reading from and writing to Starknet
contract storage. It includes traits and implementations for storing various data types
efficiently.
# Storage Architecture

- Storage addresses range from `[0, 2^251)`
- Base addresses can be combined with offsets, allowing storage of up to 255 values sequentially
- Multiple storage domains can be supported, each with its own set of storage space.
Currently, only the domain `0` is supported. Values stored in domain `0` are committed to
Ethereum as part of the state diffs.
# Core Components

- [`StorageAddress`](./core-starknet-storage_access-StorageAddress.md): Represents a specific storage location
- [`StorageBaseAddress`](./core-starknet-storage_access-StorageBaseAddress.md): Base address that can be combined with offsets
- `Store<T>`: Core trait for types that can be stored in contract storage
- `StorePacking<T,P>`: Trait for efficient packing/unpacking of values

Generally, you don't need to implement the [`Store`](./core-starknet-storage_access-Store.md) trait yourself. Most types of the core
library, at the exception of collection types, implement the [`Store`](./core-starknet-storage_access-Store.md) trait - and thus, you can
derive the [`Store`](./core-starknet-storage_access-Store.md) trait for your own types, as long as they don't contain any collections.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage_access](./core-starknet-storage_access.md)


[Traits](./core-starknet-storage_access-traits.md)
 ---
| | |
|:---|:---|
| [Store](./core-starknet-storage_access-Store.md) | Trait for types that can be stored in Starknet contract storage. The `Store`  trait enables types to be stored in and retrieved from Starknet's contract storage. Cairo implements `Store`[...](./core-starknet-storage_access-Store.md) |
| [StorePacking](./core-starknet-storage_access-StorePacking.md) | Trait for efficient packing of values into optimized storage representations. This trait enables bit-packing of complex types into simpler storage types to reduce gas costs[...](./core-starknet-storage_access-StorePacking.md) |

[Extern types](./core-starknet-storage_access-extern_types.md)
 ---
| | |
|:---|:---|
| [StorageAddress](./core-starknet-storage_access-StorageAddress.md) | Represents the address of a storage value in a Starknet contract. The value range of this type is `[0, 2**251)` .[...](./core-starknet-storage_access-StorageAddress.md) |
| [StorageBaseAddress](./core-starknet-storage_access-StorageBaseAddress.md) | Represents a base storage address that can be combined with offsets. The value range of this type is `[0, 2**251 - 256)` .[...](./core-starknet-storage_access-StorageBaseAddress.md) |

[Extern functions](./core-starknet-storage_access-extern_functions.md)
 ---
| | |
|:---|:---|
| [storage_base_address_const](./core-starknet-storage_access-storage_base_address_const.md) | Returns a `StorageBaseAddress`  given a constant `felt252`  value. The value is validated to be in the range `[0, 2**251 - 256)`  at compile time.[...](./core-starknet-storage_access-storage_base_address_const.md) |
| [storage_base_address_from_felt252](./core-starknet-storage_access-storage_base_address_from_felt252.md) | Returns a `StorageBaseAddress`  given a `felt252`  value. Wraps around the value if it is not in the range `[0, 2**251 - 256)` .[...](./core-starknet-storage_access-storage_base_address_from_felt252.md) |
| [storage_address_from_base_and_offset](./core-starknet-storage_access-storage_address_from_base_and_offset.md) | Sums the base address and the offset to return a storage address.[...](./core-starknet-storage_access-storage_address_from_base_and_offset.md) |
| [storage_address_from_base](./core-starknet-storage_access-storage_address_from_base.md) | Converts a `StorageBaseAddress`  into a `StorageAddress` . This should be used through the high-level `Into`  trait.[...](./core-starknet-storage_access-storage_address_from_base.md) |
