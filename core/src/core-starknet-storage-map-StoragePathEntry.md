# StoragePathEntry

Computes storage paths for accessing [`Map`](./core-starknet-storage-map-Map.md) entries.The storage path combines the variable's base path with the key's hash to create a unique identifier for the storage slot. This path can then be used for subsequent read or write operations, or advanced further by chaining the `entry` method.  # Examples
```cairo
use starknet::ContractAddress;
use starknet::storage::{Map, StoragePathEntry};

#[storage]
struct Storage {
    balances: Map<ContractAddress, u256>,
}

// Get the storage path for the balance of a specific address
let balance_path = self.balances.entry(address);
```

Fully qualified path: `core::starknet::storage::map::StoragePathEntry`

<pre><code class="language-rust">pub trait StoragePathEntry&lt;C&gt;</code></pre>

## Trait functions

### entry

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::entry`

<pre><code class="language-rust">fn entry(self: C, key: Self::Key) -&gt; StoragePath&lt;Self::Value&gt;</code></pre>


## Trait types

### Key

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::Key`

<pre><code class="language-rust">type Key;</code></pre>


### Value

Fully qualified path: `core::starknet::storage::map::StoragePathEntry::Value`

<pre><code class="language-rust">type Value;</code></pre>


