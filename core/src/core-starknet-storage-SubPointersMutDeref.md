# SubPointersMutDeref

This makes the sub-pointers members directly accessible from a pointer to the parent struct.

Fully qualified path: `core::starknet::storage::SubPointersMutDeref`

<pre><code class="language-rust">pub impl SubPointersMutDeref&lt;T, +SubPointersMut&lt;T&gt;&gt; of core::ops::Deref&lt;StoragePointer&lt;Mutable&lt;T&gt;&gt;&gt;</code></pre>

## Impl functions

### deref

Fully qualified path: `core::starknet::storage::SubPointersMutDeref::deref`

<pre><code class="language-rust">fn deref(self: StoragePointer&lt;Mutable&lt;T&gt;&gt;) -&gt; Self::Target</code></pre>


## Impl types

### Target

Fully qualified path: `core::starknet::storage::SubPointersMutDeref::Target`

<pre><code class="language-rust">type Target = SubPointersMut::&lt;T&gt;::SubPointersType;</code></pre>


