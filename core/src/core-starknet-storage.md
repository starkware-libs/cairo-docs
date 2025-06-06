# storage

Storage-related types and traits for Cairo contracts.
This module implements the storage system for Starknet contracts, providing high-level
abstractions for persistent data storage. It offers a type-safe interface for reading and
writing to Starknet storage through the `StoragePointerReadAccess` and
`StoragePointerWriteAccess` traits, along with useful storage-only collection types like
[`Vec`](./core-starknet-storage-vec-Vec.md) and [`Map`](./core-starknet-storage-map-Map.md).
# Overview

The storage system in Starknet contracts is built on a key-value store where each storage slot
is identified by a 251-bit address. The storage system allows interactions with storage using
state variables, which are declared inside a `Storage` struct annotated with the `#[storage]`
attribute. This ensures type-safe storage access and simplifies the process of reading and
writing to storage.
# Using the Storage System

Storage is typically declared using the `#[storage]` attribute on a struct:
```cairo
#[storage]
struct Storage {
    balance: u256,
    users: Map<ContractAddress, User>,
    nested_data: Map<ContractAddress, Map<ContractAddress, u8>>,
    collection: Vec<u8>,
}
```

Any type that implements the `Store` trait (or it's optimized `StorePacked` variant) can be used
in storage.  This type can simply be derived using `#[derive(Store)]` - provided that all of the
members of the type also implement `Store`.
```cairo
#[derive(Copy, Default, Drop, Store)]
struct User {
    name: felt252,
    age: u8,
}
```

Interaction with storage is made through a set of traits, depending on the type interacted
with:
- `StoragePointerReadAccess` and `StoragePointerWriteAccess` allow for reading and writing
storable types.
- [`StorageMapReadAccess`](./core-starknet-storage-map-StorageMapReadAccess.md) and [`StorageMapWriteAccess`](./core-starknet-storage-map-StorageMapWriteAccess.md) allow for reading and writing to
storage [`Map`](./core-starknet-storage-map-Map.md)s.
- [`StoragePathEntry`](./core-starknet-storage-map-StoragePathEntry.md) allows for accessing a specific entry in a [`Map`](./core-starknet-storage-map-Map.md), and can be combined
with the `StoragePointer` traits to read and write in these entries.
- [`VecTrait`](./core-starknet-storage-vec-VecTrait.md) and [`MutableVecTrait`](./core-starknet-storage-vec-MutableVecTrait.md) allow for interacting with storage [`Vec`](./core-starknet-storage-vec-Vec.md)s.
## Examples

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
# Storage Lifecycle

When you access a storage variable, it goes through several transformations:

1. FlattenedStorage: The starting point is your contract's storage struct. Each member is
represented either as a `StorageBase` or another `FlattenedStorage` (for `#[substorage(v0)]`
or `#[flat]` members).

2. StorageBase: For simple variables, this holds the `sn_keccak` hash of the variable name,
which becomes the storage address. For example:
```cairo
#[storage]
struct Storage {
    balance: u128,  // Stored at sn_keccak('balance')
}
```


3. StoragePath: For complex types, a `StoragePath` represents an un-finalized path to a
specific entry in storage. For example, a `StoragePath` for a `Map` can be updated with
specific keys to point to a specific entry in the map.

4. StoragePointer: The final form, pointing to the actual storage location. For multi-slot
values (like structs), values are stored sequentially from this address.
# Storage Collections

Cairo's memory collection types, like `Felt252Dict` and [`Array`](./core-array-Array.md), can not be used in storage.
Consequently, any type that contains these types can not be used in storage either.
Instead, Cairo has two storage-only collection types: [`Map`](./core-starknet-storage-map-Map.md) and [`Vec`](./core-starknet-storage-vec-Vec.md).
Instead of storing these memory collections directly, you will need to reflect them into
storage using the [`Map`](./core-starknet-storage-map-Map.md) and [`Vec`](./core-starknet-storage-vec-Vec.md) types.
# Address Calculation

Storage addresses are calculated deterministically:

- For a single value variable, the address is the `sn_keccak` hash of the variable name's ASCII
encoding. `sn_keccak` is Starknet's version of the Keccak-256 hash function, with its output
truncated to 250 bits.

- For variables composed of multiple values (tuples, structs, or enums), the base storage
address is also the `sn_keccak` hash of the variable name's ASCII encoding. The storage layout
then varies depending on the specific type. A struct will store its members as a sequence of
primitive types, while an enum will store its variant index, followed by the members of the
variant.

- For variables within a storage node, the address is calculated using a chain of hashes that
represents the node structure. Given a member `m` within a storage variable `variable_name`,
the path is computed as `h(sn_keccak(variable_name), sn_keccak(m))`, where `h` is the Pedersen
hash. For nested storage nodes, this process repeats, creating a hash chain representing the
path to each leaf node. At the leaf node, the storage calculation follows the standard rules for
that variable type.

- For [`Map`](./core-starknet-storage-map-Map.md) or [`Vec`](./core-starknet-storage-vec-Vec.md) variables, the address is calculated relative to the storage base
address (the `sn_keccak` hash of the variable name) combined with the mapping keys or vector
indices.
See their respective module documentation for more details.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage](./core-starknet-storage.md)


[Modules](./core-starknet-storage-modules.md)
 ---
| | |
|:---|:---|
| [map](./core-starknet-storage-map.md) | Key-value storage mapping implementation for Starknet contracts. This module provides the core mapping functionality used in Starknet smart contracts,[...](./core-starknet-storage-map.md) |
| [storage_base](./core-starknet-storage-storage_base.md) | Core abstractions for contract storage management. This module provides the types and traits for handling contract storage internally[...](./core-starknet-storage-storage_base.md) |
| [vec](./core-starknet-storage-vec.md) | Vector-like storage collection for persisting data in contract storage. This module provides a vector-like collection that stores elements in contract storage.[...](./core-starknet-storage-vec.md) |
| [storage_node](./core-starknet-storage-storage_node.md) | Storage nodes provide a way to structure contract storage data, reflecting their structure in the storage address computation of their members. They are special structs that can contain any[...](./core-starknet-storage-storage_node.md) |
| [sub_pointers](./core-starknet-storage-sub_pointers.md) | [...](./core-starknet-storage-sub_pointers.md) |

[Structs](./core-starknet-storage-structs.md)
 ---
| | |
|:---|:---|
| [StoragePointer](./core-starknet-storage-StoragePointer.md) | A pointer to an address in storage, can be used to read and write values, if the generic type supports it (e.g. basic types like `felt252` ).[...](./core-starknet-storage-StoragePointer.md) |
| [StoragePointer0Offset](./core-starknet-storage-StoragePointer0Offset.md) | Same as `StoragePointer` , but with `offset`  0, which allows for some optimizations.[...](./core-starknet-storage-StoragePointer0Offset.md) |
| [StoragePath](./core-starknet-storage-StoragePath.md) | An intermediate struct to store a hash state, in order to be able to hash multiple values and get the final address. Storage path should have two interfaces, if `T`[...](./core-starknet-storage-StoragePath.md) |
| [PendingStoragePath](./core-starknet-storage-PendingStoragePath.md) | A struct for delaying the creation of a storage path, used for lazy evaluation in storage nodes.[...](./core-starknet-storage-PendingStoragePath.md) |
| [Mutable](./core-starknet-storage-Mutable.md) | A wrapper around different storage related types, indicating that the instance is mutable, i.e. originally created from a `ref`  contract state.[...](./core-starknet-storage-Mutable.md) |

[Traits](./core-starknet-storage-traits.md)
 ---
| | |
|:---|:---|
| [StorageAsPointer](./core-starknet-storage-StorageAsPointer.md) | Trait for converting a storage member to a `StoragePointer0Offset` .[...](./core-starknet-storage-StorageAsPointer.md) |
| [StoragePointerReadAccess](./core-starknet-storage-StoragePointerReadAccess.md) | Trait for accessing the values in storage using a `StoragePointer` .[...](./core-starknet-storage-StoragePointerReadAccess.md) |
| [StoragePointerWriteAccess](./core-starknet-storage-StoragePointerWriteAccess.md) | Trait for writing values to storage using a `StoragePointer` .[...](./core-starknet-storage-StoragePointerWriteAccess.md) |
| [StorageAsPath](./core-starknet-storage-StorageAsPath.md) | Trait for creating a new `StoragePath`  from a storage member.[...](./core-starknet-storage-StorageAsPath.md) |
| [PendingStoragePathTrait](./core-starknet-storage-PendingStoragePathTrait.md) | A trait for creating a `PendingStoragePath`  from a `StoragePath`  hash state and a key.[...](./core-starknet-storage-PendingStoragePathTrait.md) |
| [StoragePathMutableConversion](./core-starknet-storage-StoragePathMutableConversion.md) | [...](./core-starknet-storage-StoragePathMutableConversion.md) |
| [IntoIterRange](./core-starknet-storage-IntoIterRange.md) | Trait for turning collection of values into an iterator over a specific range.[...](./core-starknet-storage-IntoIterRange.md) |
| [ValidStorageTypeTrait](./core-starknet-storage-ValidStorageTypeTrait.md) | Trait that ensures a type is valid for storage in Starknet contracts. This trait is used to enforce that only specific types, such as those implementing `Store`  or acting as a `StorageNode`[...](./core-starknet-storage-ValidStorageTypeTrait.md) |

[Impls](./core-starknet-storage-impls.md)
 ---
| | |
|:---|:---|
| [SubPointersDeref](./core-starknet-storage-SubPointersDeref.md) | This makes the sub-pointers members directly accessible from a pointer to the parent struct.[...](./core-starknet-storage-SubPointersDeref.md) |
| [SubPointersMutDeref](./core-starknet-storage-SubPointersMutDeref.md) | This makes the sub-pointers members directly accessible from a pointer to the parent struct.[...](./core-starknet-storage-SubPointersMutDeref.md) |
| [StorableStoragePointerReadAccess](./core-starknet-storage-StorableStoragePointerReadAccess.md) | Simple implementation of `StoragePointerReadAccess`  for any type that implements `Store`  for any offset.[...](./core-starknet-storage-StorableStoragePointerReadAccess.md) |
| [StorageNodeDeref](./core-starknet-storage-StorageNodeDeref.md) | This makes the storage node members directly accessible from a path to the parent struct.[...](./core-starknet-storage-StorageNodeDeref.md) |
| [StorageNodeMutDeref](./core-starknet-storage-StorageNodeMutDeref.md) | This makes the storage node members directly accessible from a path to the parent struct.[...](./core-starknet-storage-StorageNodeMutDeref.md) |
## Re-exports

 - ### Structs

| | |
|:---|:---|
| [Map](./core-starknet-storage-map-Map.md) | A persistent key-value store in contract storage. This type cannot be instantiated as it is marked with `#[phantom]` . This is by design: `Map`[...](./core-starknet-storage-map-Map.md) |
| [FlattenedStorage](./core-starknet-storage-storage_base-FlattenedStorage.md) | A type that represents a flattened storage, i.e. a storage object which does not have any effect on the path taken into consideration when computing the address of the storage object.[...](./core-starknet-storage-storage_base-FlattenedStorage.md) |
| [StorageBase](./core-starknet-storage-storage_base-StorageBase.md) | A struct for holding an address to initialize a storage path with. The members (not direct members, but accessible using `deref` ) of a contract state are either `StorageBase`  or `FlattenedStorage`[...](./core-starknet-storage-storage_base-StorageBase.md) |
| [Vec](./core-starknet-storage-vec-Vec.md) | Represents a dynamic array in contract storage. This type is zero-sized and cannot be instantiated. Vectors can only be used in storage contexts and manipulated using the associated `VecTrait` and[...](./core-starknet-storage-vec-Vec.md) |
| [VecIter](./core-starknet-storage-vec-VecIter.md) | An iterator struct over a `Vec`  in storage.[...](./core-starknet-storage-vec-VecIter.md) |

<br>


 - ### Traits

| | |
|:---|:---|
| [StorageMapReadAccess](./core-starknet-storage-map-StorageMapReadAccess.md) | Provides direct read access to values in a storage [`Map`](./core-starknet-storage-map-Map.md) .[...](./core-starknet-storage-map-StorageMapReadAccess.md) |
| [StorageMapWriteAccess](./core-starknet-storage-map-StorageMapWriteAccess.md) | Provides direct write access to values in a storage [`Map`](./core-starknet-storage-map-Map.md) . Enables directly storing values in the contract's storage at the address of the given key.[...](./core-starknet-storage-map-StorageMapWriteAccess.md) |
| [StoragePathEntry](./core-starknet-storage-map-StoragePathEntry.md) | Computes storage paths for accessing [`Map`](./core-starknet-storage-map-Map.md)  entries. The storage path combines the variable's base path with the key's hash to create a unique[...](./core-starknet-storage-map-StoragePathEntry.md) |
| [StorageTrait](./core-starknet-storage-storage_base-StorageTrait.md) | A trait for creating the struct containing the `StorageBase`  or `FlattenedStorage`  of all the members of a contract state.[...](./core-starknet-storage-storage_base-StorageTrait.md) |
| [StorageTraitMut](./core-starknet-storage-storage_base-StorageTraitMut.md) | A trait for creating the struct containing the mutable `StorageBase`  or `FlattenedStorage`  of all the members of a contract state.[...](./core-starknet-storage-storage_base-StorageTraitMut.md) |
| [StorageNode](./core-starknet-storage-storage_node-StorageNode.md) | A trait that given a storage path of a struct, generates the storage node of this struct.[...](./core-starknet-storage-storage_node-StorageNode.md) |
| [StorageNodeMut](./core-starknet-storage-storage_node-StorageNodeMut.md) | A mutable version of `StorageNode` , works the same way, but on `Mutable<T>` .[...](./core-starknet-storage-storage_node-StorageNodeMut.md) |
| [SubPointers](./core-starknet-storage-sub_pointers-SubPointers.md) | Similar to storage node, but for structs which are stored sequentially in the storage. In contrast to storage node, the fields of the struct are just at an offset from the base address of the struct.[...](./core-starknet-storage-sub_pointers-SubPointers.md) |
| [SubPointersForward](./core-starknet-storage-sub_pointers-SubPointersForward.md) | A trait for implementing `SubPointers`  for types which are not a `StoragePointer` , such as `StorageBase`  and `StoragePath` .[...](./core-starknet-storage-sub_pointers-SubPointersForward.md) |
| [SubPointersMut](./core-starknet-storage-sub_pointers-SubPointersMut.md) | A mutable version of `SubPointers` , works the same way, but on `Mutable<T>` .[...](./core-starknet-storage-sub_pointers-SubPointersMut.md) |
| [SubPointersMutForward](./core-starknet-storage-sub_pointers-SubPointersMutForward.md) | A trait for implementing `SubPointersMut`  for types which are not a `StoragePointer` , such as `StorageBase`  and `StoragePath` .[...](./core-starknet-storage-sub_pointers-SubPointersMutForward.md) |
| [MutableVecTrait](./core-starknet-storage-vec-MutableVecTrait.md) | Provides mutable access to elements in a storage [`Vec`](./core-starknet-storage-vec-Vec.md) . This trait extends the read functionality with methods to append new elements and modify existing ones.[...](./core-starknet-storage-vec-MutableVecTrait.md) |
| [VecTrait](./core-starknet-storage-vec-VecTrait.md) | Provides read-only access to elements in a storage [`Vec`](./core-starknet-storage-vec-Vec.md) . This trait enables retrieving elements and checking the vector's length without[...](./core-starknet-storage-vec-VecTrait.md) |

<br>

