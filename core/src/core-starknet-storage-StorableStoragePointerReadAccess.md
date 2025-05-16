# StorableStoragePointerReadAccess

Simple implementation of `StoragePointerReadAccess` for any type that implements `Store` for any offset.

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess`

<pre><code class="language-rust">pub impl StorableStoragePointerReadAccess&lt;
    T, +starknet::Store&lt;T&gt;,
&gt; of StoragePointerReadAccess&lt;StoragePointer&lt;T&gt;&gt;</code></pre>

## Impl functions

### read

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess::read`

<pre><code class="language-rust">fn read(self: @StoragePointer&lt;T&gt;) -&gt; T</code></pre>


## Impl types

### Value

Fully qualified path: `core::starknet::storage::StorableStoragePointerReadAccess::Value`

<pre><code class="language-rust">type Value = T;</code></pre>


