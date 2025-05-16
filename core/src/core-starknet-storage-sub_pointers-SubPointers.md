# SubPointers

Similar to storage node, but for structs which are stored sequentially in the storage. In contrast to storage node, the fields of the struct are just at an offset from the base address of the struct.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers`

<pre><code class="language-rust">pub trait SubPointers&lt;T&gt;</code></pre>

## Trait functions

### sub_pointers

Creates a sub pointers struct for the given storage pointer to a struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers::sub_pointers`

<pre><code class="language-rust">fn sub_pointers(self: StoragePointer&lt;T&gt;) -&gt; Self::SubPointersType</code></pre>


## Trait types

### SubPointersType

The type of the storage pointers, generated for the struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointers::SubPointersType`

<pre><code class="language-rust">type SubPointersType;</code></pre>


