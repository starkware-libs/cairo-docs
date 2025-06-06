# VecIter

An iterator struct over a `Vec` in storage.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage](./core-starknet-storage.md)::[vec](./core-starknet-storage-vec.md)::[VecIter](./core-starknet-storage-vec-VecIter.md)

<pre><code class="language-cairo">#[derive(Drop)]
pub struct VecIter&lt;T, impl VecTraitImpl: <a href="core-starknet-storage-vec-VecTrait.html">VecTrait</a>&lt;T&gt;&gt; {
    vec: T,
    current_index: <a href="core-ops-range-internal-IntRange.html">IntRange&lt;u64&gt;</a>,
}</code></pre>

