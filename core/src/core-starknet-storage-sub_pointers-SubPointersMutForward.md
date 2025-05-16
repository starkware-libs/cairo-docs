# SubPointersMutForward

A trait for implementing `SubPointersMut` for types which are not a `StoragePointer`, such as `StorageBase` and `StoragePath`.

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward`

<pre><code class="language-rust">pub trait SubPointersMutForward&lt;T&gt;</code></pre>

## Trait functions

### sub_pointers_mut

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward::sub_pointers_mut`

<pre><code class="language-rust">fn sub_pointers_mut(self: T) -&gt; Self::SubPointersType</code></pre>


## Trait types

### SubPointersType

Fully qualified path: `core::starknet::storage::sub_pointers::SubPointersMutForward::SubPointersType`

<pre><code class="language-rust">type SubPointersType;</code></pre>


