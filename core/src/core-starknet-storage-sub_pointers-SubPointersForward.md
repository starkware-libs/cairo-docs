# SubPointersForward

A trait for implementing `SubPointers` for types which are not a `StoragePointer`, such as `StorageBase` and `StoragePath`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward`

<pre><code class="language-rust">pub trait SubPointersForward&lt;T&gt;</code></pre>

## Trait functions

### sub_pointers

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward::sub_pointers`

<pre><code class="language-rust">fn sub_pointers(self: T) -&gt; Self::SubPointersType</code></pre>


## Trait types

### SubPointersType

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersForward::SubPointersType`

<pre><code class="language-rust">type SubPointersType;</code></pre>


