# StorageNodeMutDeref

This makes the storage node members directly accessible from a path to the parent struct.

Fully qualified path: `core::starknet::storage::StorageNodeMutDeref`

<pre><code class="language-rust">pub impl StorageNodeMutDeref&lt;T, +StorageNodeMut&lt;T&gt;&gt; of core::ops::Deref&lt;StoragePath&lt;Mutable&lt;T&gt;&gt;&gt;</code></pre>

## Impl functions

### deref

Fully qualified path: `core::starknet::storage::StorageNodeMutDeref::deref`

<pre><code class="language-rust">fn deref(self: StoragePath&lt;Mutable&lt;T&gt;&gt;) -&gt; Self::Target</code></pre>


## Impl types

### Target

Fully qualified path: `core::starknet::storage::StorageNodeMutDeref::Target`

<pre><code class="language-rust">type Target = StorageNodeMut::&lt;T&gt;::NodeType;</code></pre>


