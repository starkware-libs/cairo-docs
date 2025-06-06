# storage_base

Core abstractions for contract storage management.
This module provides the types and traits for handling contract storage internally
within the Cairo core library. Most developers should not need to implement these traits
directly, as they are primarily used by the storage system implementation.
If you're writing a regular Starknet contract, you should use the high-level storage
traits and types, interacting with the members of the storage struct directly.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage](./core-starknet-storage.md)::[storage_base](./core-starknet-storage-storage_base.md)


[Structs](./core-starknet-storage-storage_base-structs.md)
 ---
| | |
|:---|:---|
| [FlattenedStorage](./core-starknet-storage-storage_base-FlattenedStorage.md) | A type that represents a flattened storage, i.e. a storage object which does not have any effect on the path taken into consideration when computing the address of the storage object.[...](./core-starknet-storage-storage_base-FlattenedStorage.md) |
| [StorageBase](./core-starknet-storage-storage_base-StorageBase.md) | A struct for holding an address to initialize a storage path with. The members (not direct members, but accessible using `deref` ) of a contract state are either `StorageBase`  or `FlattenedStorage`[...](./core-starknet-storage-storage_base-StorageBase.md) |

[Traits](./core-starknet-storage-storage_base-traits.md)
 ---
| | |
|:---|:---|
| [StorageTrait](./core-starknet-storage-storage_base-StorageTrait.md) | A trait for creating the struct containing the `StorageBase`  or `FlattenedStorage`  of all the members of a contract state.[...](./core-starknet-storage-storage_base-StorageTrait.md) |
| [StorageTraitMut](./core-starknet-storage-storage_base-StorageTraitMut.md) | A trait for creating the struct containing the mutable `StorageBase`  or `FlattenedStorage`  of all the members of a contract state.[...](./core-starknet-storage-storage_base-StorageTraitMut.md) |
