# map

Key-value storage mapping implementation for Starknet contracts.
This module provides the core mapping functionality used in Starknet smart contracts,
enabling persistent key-value storage. Unlike traditional hash tables, storage mappings
do not store the key data itself. Instead, they use the hash of the key to compute
a storage slot address where the corresponding value is stored.
# Interacting with [`Map`](./core-starknet-storage-map-Map.md)

Storage maps can be accessed through two sets of traits, each serving different use cases:

1. Direct access using `StorageMapReadAccess`/`StorageMapWriteAccess`:
These traits allow you to read from or write to a map directly by providing the key(s)
and value:
```cairo
// Read directly with key
let value = self.my_map.read(key);

// Write directly with key and value
self.my_map.write(key, value);
```


2. Path-based access combining `StoragePathEntry` with
`StoragePointerReadAccess`/`StoragePointerWriteAccess`:
This approach first computes a `StoragePath` for the entry, which can then be used with
the `StoragePointer` access traits from `starknet::storage`:
```cairo
// Get storage path for the entry
let path = self.my_map.entry(key);

// Read/write using the storage pointer traits
let value = path.read();
path.write(new_value);
```


The path-based approach is particularly useful for:
- Nested mappings where you need to chain multiple keys
- Cases where you need to reuse the same storage path multiple times
# Storage Address Computation

Storage addresses for mapping entries are deterministically computed using hash functions:

- For a single key mapping:
```text
address = h(sn_keccak(variable_name), k) mod N
```

where:
    - `h` is the Pedersen hash function
    - `k` is the key value
    - `N` is 2^251 - 256

- For nested mappings with multiple keys:
```text
address = h(h(...h(h(sn_keccak(variable_name), k₁), k₂)...), kₙ) mod N
```

where each key `kᵢ` is hashed sequentially with the result of the previous hash.
# Examples

Basic usage with a single mapping:
```cairo
use starknet::ContractAddress;
use starknet::storage::{Map, StorageMapReadAccess, StoragePathEntry,
StoragePointerReadAccess};

#[storage]
struct Storage {
    balances: Map<ContractAddress, u256>,
}

fn read_storage(self: @ContractState, address: ContractAddress) {
    let balance = self.balances.read(address);
    let balance = self.balances.entry(address).read();
}
```

Nested mappings:
```cairo
#[storage]
struct Storage {
    allowances: Map<ContractAddress, Map<ContractAddress, u256>>,
}

fn read_storage(self: @ContractState, owner: ContractAddress, spender: ContractAddress) {
    let allowance = self.allowances.entry(owner).entry(spender).read();
    let allowance = self.allowances.entry(owner).read(spender);
}
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage](./core-starknet-storage.md)::[map](./core-starknet-storage-map.md)


[Structs](./core-starknet-storage-map-structs.md)
 ---
| | |
|:---|:---|
| [Map](./core-starknet-storage-map-Map.md) | A persistent key-value store in contract storage. This type cannot be instantiated as it is marked with `#[phantom]` . This is by design: `Map`[...](./core-starknet-storage-map-Map.md) |

[Traits](./core-starknet-storage-map-traits.md)
 ---
| | |
|:---|:---|
| [StorageMapReadAccess](./core-starknet-storage-map-StorageMapReadAccess.md) | Provides direct read access to values in a storage [`Map`](./core-starknet-storage-map-Map.md) .[...](./core-starknet-storage-map-StorageMapReadAccess.md) |
| [StorageMapWriteAccess](./core-starknet-storage-map-StorageMapWriteAccess.md) | Provides direct write access to values in a storage [`Map`](./core-starknet-storage-map-Map.md) . Enables directly storing values in the contract's storage at the address of the given key.[...](./core-starknet-storage-map-StorageMapWriteAccess.md) |
| [StoragePathEntry](./core-starknet-storage-map-StoragePathEntry.md) | Computes storage paths for accessing [`Map`](./core-starknet-storage-map-Map.md)  entries. The storage path combines the variable's base path with the key's hash to create a unique[...](./core-starknet-storage-map-StoragePathEntry.md) |
