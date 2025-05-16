# SubPointersDeref

This makes the sub-pointers members directly accessible from a pointer to the parent struct.

Fully qualified path: `core::starknet::storage::SubPointersDeref`

<pre><code class="language-rust">pub impl SubPointersDeref&lt;T, +SubPointers&lt;T&gt;&gt; of core::ops::Deref&lt;StoragePointer&lt;T&gt;&gt;</code></pre>

## Impl functions

### deref

Fully qualified path: `core::starknet::storage::SubPointersDeref::deref`

<pre><code class="language-rust">fn deref(self: StoragePointer&lt;T&gt;) -&gt; Self::Target</code></pre>


## Impl types

### Target

Fully qualified path: `core::starknet::storage::SubPointersDeref::Target`

<pre><code class="language-rust">type Target = SubPointers::&lt;T&gt;::SubPointersType;</code></pre>


