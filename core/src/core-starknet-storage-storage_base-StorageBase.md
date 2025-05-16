# StorageBase

A struct for holding an address to initialize a storage path with. The members (not direct members, but accessible using `deref`) of a contract state are either `StorageBase` or `FlattenedStorage` instances, with the generic type representing the type of the stored member.

Fully qualified path: `core::starknet::storage::storage_base::StorageBase`

<pre><code class="language-rust">pub struct StorageBase&lt;T&gt; {
    pub __base_address__: felt252,
}</code></pre>

## Members

### __base_address__

Fully qualified path: `core::starknet::storage::storage_base::StorageBase::__base_address__`

<pre><code class="language-rust">pub __base_address__: felt252</code></pre>


