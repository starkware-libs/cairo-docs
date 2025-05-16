# SubPointersMut

A mutable version of `SubPointers`, works the same way, but on `Mutable<T>`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut`

<pre><code class="language-rust">pub trait SubPointersMut&lt;T&gt;</code></pre>

## Trait functions

### sub_pointers_mut

Creates a sub pointers struct for the given storage pointer to a struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut::sub_pointers_mut`

<pre><code class="language-rust">fn sub_pointers_mut(self: StoragePointer&lt;Mutable&lt;T&gt;&gt;) -&gt; Self::SubPointersType</code></pre>


## Trait types

### SubPointersType

The type of the storage pointers, generated for the struct T.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMut::SubPointersType`

<pre><code class="language-rust">type SubPointersType;</code></pre>


