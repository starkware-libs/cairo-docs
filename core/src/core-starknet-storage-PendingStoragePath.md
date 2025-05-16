# PendingStoragePath

A struct for delaying the creation of a storage path, used for lazy evaluation in storage nodes.

Fully qualified path: `core::starknet::storage::PendingStoragePath`

<pre><code class="language-rust">pub struct PendingStoragePath&lt;T&gt; {
    __hash_state__: StoragePathHashState,
    __pending_key__: felt252,
}</code></pre>

