# StorageTraitMut

A trait for creating the struct containing the mutable `StorageBase` or `FlattenedStorage` of all the members of a contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut`

<pre><code class="language-rust">pub trait StorageTraitMut&lt;T&gt;</code></pre>

## Trait functions

### storage_mut

Creates a struct containing a mutable version of the `StorageBase` or `FlattenedStorage` of all the members of a contract state. Should be called from the `deref` method of the contract state.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut::storage_mut`

<pre><code class="language-rust">fn storage_mut(self: FlattenedStorage&lt;Mutable&lt;T&gt;&gt;) -&gt; Self::BaseType</code></pre>


## Trait types

### BaseType

The type of the struct containing the mutable `StorageBase` or `FlattenedStorage` of all the members of the type `T`.

Fully qualified path: `core::starknet::storage::storage_base::StorageTraitMut::BaseType`

<pre><code class="language-rust">type BaseType;</code></pre>


