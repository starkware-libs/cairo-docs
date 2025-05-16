# StorageNodeDeref

This makes the storage node members directly accessible from a path to the parent struct.

Fully qualified path: `core::starknet::storage::StorageNodeDeref`

<pre><code class="language-rust">pub impl StorageNodeDeref&lt;T, +StorageNode&lt;T&gt;&gt; of core::ops::Deref&lt;StoragePath&lt;T&gt;&gt;</code></pre>

## Impl functions

### deref

Fully qualified path: `core::starknet::storage::StorageNodeDeref::deref`

<pre><code class="language-rust">fn deref(self: StoragePath&lt;T&gt;) -&gt; Self::Target</code></pre>


## Impl types

### Target

Fully qualified path: `core::starknet::storage::StorageNodeDeref::Target`

<pre><code class="language-rust">type Target = StorageNode::&lt;T&gt;::NodeType;</code></pre>


