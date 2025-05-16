# StorageTrait

A trait for creating the struct containing the `StorageBase` or `FlattenedStorage` of all the members of a contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait`

<pre><code class="language-rust">pub trait StorageTrait&lt;T&gt;</code></pre>

## Trait functions

### storage

Creates a struct containing the `StorageBase` or `FlattenedStorage` of all the members of a contract state. Should be called from the `deref` method of the contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait::storage`

<pre><code class="language-rust">fn storage(self: FlattenedStorage&lt;T&gt;) -&gt; Self::BaseType</code></pre>


## Trait types

### BaseType

The type of the struct containing the `StorageBase` or `FlattenedStorage` of all the members of the type `T`.

Fully qualified path: `core::starknet::storage::storage_base::StorageTrait::BaseType`

<pre><code class="language-rust">type BaseType;</code></pre>


