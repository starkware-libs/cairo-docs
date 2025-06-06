
[Structs](./core-starknet-storage-structs.md)
 ---
| | |
|:---|:---|
| [StoragePointer](./core-starknet-storage-StoragePointer.md) | A pointer to an address in storage, can be used to read and write values, if the generic type supports it (e.g. basic types like `felt252` ).[...](./core-starknet-storage-StoragePointer.md) |
| [StoragePointer0Offset](./core-starknet-storage-StoragePointer0Offset.md) | Same as `StoragePointer` , but with `offset`  0, which allows for some optimizations.[...](./core-starknet-storage-StoragePointer0Offset.md) |
| [StoragePath](./core-starknet-storage-StoragePath.md) | An intermediate struct to store a hash state, in order to be able to hash multiple values and get the final address. Storage path should have two interfaces, if `T`[...](./core-starknet-storage-StoragePath.md) |
| [PendingStoragePath](./core-starknet-storage-PendingStoragePath.md) | A struct for delaying the creation of a storage path, used for lazy evaluation in storage nodes.[...](./core-starknet-storage-PendingStoragePath.md) |
| [Mutable](./core-starknet-storage-Mutable.md) | A wrapper around different storage related types, indicating that the instance is mutable, i.e. originally created from a `ref`  contract state.[...](./core-starknet-storage-Mutable.md) |
