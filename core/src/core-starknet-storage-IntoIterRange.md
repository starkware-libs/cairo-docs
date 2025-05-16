# IntoIterRange

Trait for turning collection of values into an iterator over a specific range.

Fully qualified path: `core::starknet::storage::IntoIterRange`

<pre><code class="language-rust">pub trait IntoIterRange&lt;T&gt;</code></pre>

## Trait functions

### into_iter_range

Creates an iterator over a range from a collection.

Fully qualified path: `core::starknet::storage::IntoIterRange::into_iter_range`

<pre><code class="language-rust">fn into_iter_range(self: T, range: core::ops::Range&lt;u64&gt;) -&gt; Self::IntoIter</code></pre>


### into_iter_full_range

Creates an iterator over the full range of a collection.

Fully qualified path: `core::starknet::storage::IntoIterRange::into_iter_full_range`

<pre><code class="language-rust">fn into_iter_full_range(self: T) -&gt; Self::IntoIter</code></pre>


## Trait types

### IntoIter

Fully qualified path: `core::starknet::storage::IntoIterRange::IntoIter`

<pre><code class="language-rust">type IntoIter;</code></pre>


