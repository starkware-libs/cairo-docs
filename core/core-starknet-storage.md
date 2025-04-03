# storage

This module contains the storage-related types and traits for Cairo contracts. It provides abstractions for reading and writing to Starknet storage.  The front facing interface for the user is simple and intuitive, for example consider the following storage struct:
```cairo
#[storage]
struct Storage {
    a: felt252,
    b: Map<felt252, felt52>,
    c: Map<felt52, Map<felt52, felt52>>,
}
```
The user can access the storage members `a` and `b` using the following code:
```cairo
fn use_storage(self: @ContractState) {
    let a_value = self.a.read();
    // For a Map, the user can use the `entry` method to access the value at a specific key:
    let b_value = self.b.entry(42).read();
    // Or simply pass the key to the `read` method:
    let b_value = self.b.read(42);
    // Accessing a nested Map must be done using the `entry` method, either:
    let c_value = self.c.entry(42).entry(43).read()
    // Or:
    let c_value = self.c.entry(42).read(43);
}
```
Under the hood, the storage access is more complex. The life cycle of a storage object is as follows: 1. The storage struct of a contract is represented by a `FlattenedStorage` struct, which    can be derefed into a struct containing a member for each storage member of the contract.    This member can be either a `StorageBase` or a `FlattenedStorage` instance. Members are    represented as a `FlattenedStorage` if the storage member is attributed with either    `#[substorage(v0)]` (for backward compatibility) or `#[flat]`. `FlattenedStorage` is used to    structure the storage access; however, it does not affect the address of the storage object. 2. `StorageBase` members of a `FlattenedStorage` struct hold a single `felt252` value, which is    the Keccak hash of the name of the member. For simple types, this value will be the address    of the member in the storage. 3. `StorageBase` members are then converted to `StoragePath` instances, which are essentially    a wrapper around a `HashState` instance, used to account for more values when computing the    address of the storage object. `StoragePath` instances can be updated with values coming from    two sources:- Storage nodes, which are structs that represent another struct with all its members
  in the storage, similar to `FlattenedStorage`. However, unlike `FlattenedStorage`, the
  path to the storage node does affect the address of the storage object. See `StorageNode`
  for more details.
- Storage collections, specifically `Map` and `Vec`, simulate the behavior of collections by
  updating the hash state with the key or index of the collection member.
After finishing the updates, the `StoragePath` instance is finalized, resulting in a`StoragePointer0Offset` instance, which is a pointer to the address of the storage object. Ifthe pointer is to an object of size greater than 1, the object is stored in a sequentialmanner starting from the address of the pointer. The whole object can be read or writtenusing `read` and `write` methods, and specific members can also be accessed in the case of astruct. See `SubPointers` for more details.The transitioning between the different types of storage objects is also called from the`Deref` trait, and thus, allowing an access to the members of the storage object in a simpleway.The types mentioned above are generic in the stored object type. This is done to providespecific behavior for each type of stored object, e.g., a `StoragePath` of `Map` type will havean `entry` method, but it won't have a `read` or `write` method, as `Map` is not storable byitself, only its values are.The generic type of the storage object can also be wrapped with a `Mutable` type, whichindicates that the storage object is mutable, i.e., it was created from a `ref` contract state,and thus the object can be written to.

Fully qualified path: `core::starknet::storage`

## Structs

- [StoragePointer](./core-starknet-storage-StoragePointer.md)

- [StoragePointer0Offset](./core-starknet-storage-StoragePointer0Offset.md)

- [StoragePath](./core-starknet-storage-StoragePath.md)

- [PendingStoragePath](./core-starknet-storage-PendingStoragePath.md)

- [Mutable](./core-starknet-storage-Mutable.md)

- [Vec](./core-starknet-storage-vec-Vec.md)

- [StorageBase](./core-starknet-storage-storage_base-StorageBase.md)

- [FlattenedStorage](./core-starknet-storage-storage_base-FlattenedStorage.md)

- [Map](./core-starknet-storage-map-Map.md)

## Traits

- [StorageAsPointer](./core-starknet-storage-StorageAsPointer.md)

- [StoragePointerReadAccess](./core-starknet-storage-StoragePointerReadAccess.md)

- [StoragePointerWriteAccess](./core-starknet-storage-StoragePointerWriteAccess.md)

- [StorageAsPath](./core-starknet-storage-StorageAsPath.md)

- [PendingStoragePathTrait](./core-starknet-storage-PendingStoragePathTrait.md)

- [VecTrait](./core-starknet-storage-vec-VecTrait.md)

- [MutableVecTrait](./core-starknet-storage-vec-MutableVecTrait.md)

- [StorageNode](./core-starknet-storage-storage_node-StorageNode.md)

- [StorageNodeMut](./core-starknet-storage-storage_node-StorageNodeMut.md)

- [SubPointers](./core-starknet-storage-sub_pointers-SubPointers.md)

- [SubPointersMut](./core-starknet-storage-sub_pointers-SubPointersMut.md)

- [SubPointersForward](./core-starknet-storage-sub_pointers-SubPointersForward.md)

- [SubPointersMutForward](./core-starknet-storage-sub_pointers-SubPointersMutForward.md)

- [StorageTrait](./core-starknet-storage-storage_base-StorageTrait.md)

- [StorageTraitMut](./core-starknet-storage-storage_base-StorageTraitMut.md)

- [StorageMapReadAccess](./core-starknet-storage-map-StorageMapReadAccess.md)

- [StorageMapWriteAccess](./core-starknet-storage-map-StorageMapWriteAccess.md)

- [StoragePathEntry](./core-starknet-storage-map-StoragePathEntry.md)

## Impls

- [StorableStoragePointerReadAccess](./core-starknet-storage-StorableStoragePointerReadAccess.md)

