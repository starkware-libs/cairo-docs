# storage

Storage-related types and traits for Cairo contracts.This module implements the storage system for Starknet contracts, providing high-level abstractions for persistent data storage. It offers a type-safe interface for reading and writing to Starknet storage through the [`StoragePointerReadAccess`](`StoragePointerReadAccess`) and [`StoragePointerWriteAccess`](`StoragePointerWriteAccess`) traits, along with useful storage-only collection types like [`Vec`](`Vec`) and [`Map`](`Map`).[`Vec`](`Vec`): starknet::storage::vec::Vec [`Map`](`Map`): starknet::storage::map::Map  # OverviewThe storage system in Starknet contracts is built on a key-value store where each storage slot is identified by a 251-bit address. The storage system allows interactions with storage using state variables, which are declared inside a `Storage` struct annotated with the `#[storage]` attribute. This ensures type-safe storage access and simplifies the process of reading and writing to storage.  # Using the Storage SystemStorage is typically declared using the `#[storage]` attribute on a struct:
```cairo
#[storage]
struct Storage {
    balance: u256,
    users: Map<ContractAddress, User>,
    nested_data: Map<ContractAddress, Map<ContractAddress, u8>>,
    collection: Vec<u8>,
}
```
Any type that implements the `Store` trait (or it's optimized `StorePacked` variant) can be used in storage.  This type can simply be derived using `#[derive(Store)]` - provided that all of the members of the type also implement `Store`.
```cairo
#[derive(Copy, Default, Drop, Store)]
struct User {
    name: felt252,
    age: u8,
}
```
Interaction with storage is made through a set of traits, depending on the type interacted with:[`StoragePointerReadAccess`](`StoragePointerReadAccess`) and [`StoragePointerWriteAccess`](`StoragePointerWriteAccess`) allow for reading and writing storable types. - [`StorageMapReadAccess`](`StorageMapReadAccess`) and [`StorageMapWriteAccess`](`StorageMapWriteAccess`) allow for reading and writing to storage [`Map`](`Map`)s. - [`StoragePathEntry`](`StoragePathEntry`) allows for accessing a specific entry in a [`Map`](`Map`), and can be combined with the `StoragePointer` traits to read and write in these entries. - [`VecTrait`](`VecTrait`) and [`MutableVecTrait`](`MutableVecTrait`) allow for interacting with storage [`Vec`](`Vec`)s.[`VecTrait`](`VecTrait`): starknet::storage::vec::VecTrait [`MutableVecTrait`](`MutableVecTrait`): starknet::storage::vec::MutableVecTrait [`StorageMapReadAccess`](`StorageMapReadAccess`): starknet::storage::map::StorageMapReadAccess [`StorageMapWriteAccess`](`StorageMapWriteAccess`): starknet::storage::map::StorageMapWriteAccess [`StoragePathEntry`](`StoragePathEntry`): starknet::storage::map::StoragePathEntry  ## Examples
```cairo
fn use_storage(self: @ContractState) {
    let address = 'address'.try_into().unwrap();
    // Reading values
    let balance = self.balance.read();
    // For a `Map`, use the `entry` method to access values at specific keys:
    let user = self.users.entry(address).read();
    // Accessing nested `Map`s requires chaining `entry` calls:
    let nested = self.nested_data.entry(address).entry(address).read();
    // Accessing a specific index in a `Vec` requires using the `index` method:
    let element = self.collection[index];

    // Writing values
    self.balance.write(100);
    self.users.entry(address).write(Default::default());
    self.nested_data.entry(address).entry(address).write(10);
    self.collection[index].write(20);
}
```
  # Storage LifecycleWhen you access a storage variable, it goes through several transformations:FlattenedStorage: The starting point is your contract's storage struct. Each member is represented either as a `StorageBase` or another `FlattenedStorage` (for `#[substorage(v0)]` or `#[flat]` members).StorageBase: For simple variables, this holds the `sn_keccak` hash of the variable name, which becomes the storage address. For example:
```
#[storage]
struct Storage {
    balance: u128,  // Stored at sn_keccak('balance')
}
```
StoragePath: For complex types, a `StoragePath` represents an un-finalized path to aspecific entry in storage. For example, a `StoragePath` for a `Map` can be updated withspecific keys to point to a specific entry in the map.StoragePointer: The final form, pointing to the actual storage location. For multi-slotvalues (like structs), values are stored sequentially from this address.  # Storage CollectionsCairo's memory collection types, like [`Felt252Dict`](`Felt252Dict`) and [`Array`](./core-array-Array.md), can not be used in storage.Consequently, any type that contains these types can not be used in storage either.Instead, Cairo has two storage-only collection types: [`Map`](`Map`) and [`Vec`](`Vec`).Instead of storing these memory collections directly, you will need to reflect them intostorage using the [`Map`](`Map`) and [`Vec`](`Vec`) types.  # Address CalculationStorage addresses are calculated deterministically:For a single value variable, the address is the `sn_keccak` hash of the variable name's ASCIIencoding. `sn_keccak` is Starknet's version of the Keccak-256 hash function, with its outputtruncated to 250 bits.For variables composed of multiple values (tuples, structs, or enums), the base storageaddress is also the `sn_keccak` hash of the variable name's ASCII encoding. The storage layoutthen varies depending on the specific type. A struct will store its members as a sequence ofprimitive types, while an enum will store its variant index, followed by the members of thevariant.For variables within a storage node, the address is calculated using a chain of hashes thatrepresents the node structure. Given a member `m` within a storage variable `variable_name`,the path is computed as `h(sn_keccak(variable_name), sn_keccak(m))`, where `h` is the Pedersenhash. For nested storage nodes, this process repeats, creating a hash chain representing thepath to each leaf node. At the leaf node, the storage calculation follows the standard rules forthat variable type.For [`Map`](`Map`) or [`Vec`](`Vec`) variables, the address is calculated relative to the storage baseaddress (the `sn_keccak` hash of the variable name) combined with the mapping keys or vectorindices.See their respective module documentation for more details.

Fully qualified path: `core::starknet::storage`

## Structs

- [StoragePointer](./core-starknet-storage-StoragePointer.md)

- [StoragePointer0Offset](./core-starknet-storage-StoragePointer0Offset.md)

- [StoragePath](./core-starknet-storage-StoragePath.md)

- [PendingStoragePath](./core-starknet-storage-PendingStoragePath.md)

- [Mutable](./core-starknet-storage-Mutable.md)

- [Map](./core-starknet-storage-map-Map.md)

- [FlattenedStorage](./core-starknet-storage-storage_base-FlattenedStorage.md)

- [StorageBase](./core-starknet-storage-storage_base-StorageBase.md)

- [Vec](./core-starknet-storage-vec-Vec.md)

## Traits

- [StorageAsPointer](./core-starknet-storage-StorageAsPointer.md)

- [StoragePointerReadAccess](./core-starknet-storage-StoragePointerReadAccess.md)

- [StoragePointerWriteAccess](./core-starknet-storage-StoragePointerWriteAccess.md)

- [StorageAsPath](./core-starknet-storage-StorageAsPath.md)

- [PendingStoragePathTrait](./core-starknet-storage-PendingStoragePathTrait.md)

- [IntoIterRange](./core-starknet-storage-IntoIterRange.md)

- [ValidStorageTypeTrait](./core-starknet-storage-ValidStorageTypeTrait.md)

- [StorageMapReadAccess](./core-starknet-storage-map-StorageMapReadAccess.md)

- [StorageMapWriteAccess](./core-starknet-storage-map-StorageMapWriteAccess.md)

- [StoragePathEntry](./core-starknet-storage-map-StoragePathEntry.md)

- [StorageTrait](./core-starknet-storage-storage_base-StorageTrait.md)

- [StorageTraitMut](./core-starknet-storage-storage_base-StorageTraitMut.md)

- [StorageNode](./core-starknet-storage-storage_node-StorageNode.md)

- [StorageNodeMut](./core-starknet-storage-storage_node-StorageNodeMut.md)

- [SubPointers](./core-starknet-storage-sub_pointers-SubPointers.md)

- [SubPointersForward](./core-starknet-storage-sub_pointers-SubPointersForward.md)

- [SubPointersMut](./core-starknet-storage-sub_pointers-SubPointersMut.md)

- [SubPointersMutForward](./core-starknet-storage-sub_pointers-SubPointersMutForward.md)

- [MutableVecTrait](./core-starknet-storage-vec-MutableVecTrait.md)

- [VecTrait](./core-starknet-storage-vec-VecTrait.md)

## Impls

- [SubPointersDeref](./core-starknet-storage-SubPointersDeref.md)

- [SubPointersMutDeref](./core-starknet-storage-SubPointersMutDeref.md)

- [StorableStoragePointerReadAccess](./core-starknet-storage-StorableStoragePointerReadAccess.md)

- [StorageNodeDeref](./core-starknet-storage-StorageNodeDeref.md)

- [StorageNodeMutDeref](./core-starknet-storage-StorageNodeMutDeref.md)

