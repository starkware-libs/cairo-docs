# StorageMapWriteAccess

Provides direct write access to values in a storage [`Map`](./core-starknet-storage-map-Map.md).Enables directly storing values in the contract's storage at the address of the given key.  # Examples
```cairo
use starknet::ContractAddress;
use starknet::storage::{Map, StorageMapWriteAccess, StoragePathEntry};

#[storage]
struct Storage {
    balances: Map<ContractAddress, u256>,
    allowances: Map<ContractAddress, Map<ContractAddress, u256>>,
}

fn write_storage(ref self: ContractState, address: ContractAddress) {
    // Write to single mapping
    self.balances.write(address, 100);
    // Write to nested mapping
    self.allowances.entry(owner).write(spender, 50);
}
```

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess`

<pre><code class="language-rust">pub trait StorageMapWriteAccess&lt;TMemberState&gt;</code></pre>

## Trait functions

### write

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::write`

<pre><code class="language-rust">fn write(self: TMemberState, key: Self::Key, value: Self::Value)</code></pre>


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::Key`

<pre><code class="language-rust">type Key;</code></pre>


### Value

Fully qualified path: `core::starknet::storage::map::StorageMapWriteAccess::Value`

<pre><code class="language-rust">type Value;</code></pre>


