# StorageMapReadAccess

Provides direct read access to values in a storage [`Map`](./core-starknet-storage-map-Map.md).  # Examples
```cairo
use starknet::ContractAddress;
use starknet::storage::{Map, StorageMapReadAccess, StoragePathEntry};

#[storage]
struct Storage {
    balances: Map<ContractAddress, u256>,
    allowances: Map<ContractAddress, Map<ContractAddress, u256>>,
}

fn read_storage(self: @ContractState, address: ContractAddress) {
    // Read from single mapping
    let balance = self.balances.read(address);
    // Read from nested mapping
    let allowance = self.allowances.entry(owner).read(spender);
}
```

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess`

<pre><code class="language-rust">pub trait StorageMapReadAccess&lt;TMemberState&gt;</code></pre>

## Trait functions

### read

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::read`

<pre><code class="language-rust">fn read(self: TMemberState, key: Self::Key) -&gt; Self::Value</code></pre>


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::Key`

<pre><code class="language-rust">type Key;</code></pre>


### Value

Fully qualified path: `core::starknet::storage::map::StorageMapReadAccess::Value`

<pre><code class="language-rust">type Value;</code></pre>


