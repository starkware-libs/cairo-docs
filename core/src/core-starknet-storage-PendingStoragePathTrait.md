# PendingStoragePathTrait

A trait for creating a `PendingStoragePath` from a `StoragePath` hash state and a key.

Fully qualified path: `core::starknet::storage::PendingStoragePathTrait`

<pre><code class="language-rust">pub trait PendingStoragePathTrait&lt;T, S&gt;</code></pre>

## Trait functions

### new

Fully qualified path: `core::starknet::storage::PendingStoragePathTrait::new`

<pre><code class="language-rust">fn new(storage_path: @StoragePath&lt;S&gt;, pending_key: felt252) -&gt; PendingStoragePath&lt;T&gt;</code></pre>


