# QM31Trait

Fully qualified path: [core](./core.md)::[qm31](./core-qm31.md)::[QM31Trait](./core-qm31-QM31Trait.md)

<pre><code class="language-cairo">pub trait QM31Trait</code></pre>

## Trait functions

### new

Returns a new `qm31` composed of the given parts.

Fully qualified path: [core](./core.md)::[qm31](./core-qm31.md)::[QM31Trait](./core-qm31-QM31Trait.md)::[new](./core-qm31-QM31Trait.md#new)

<pre><code class="language-cairo">fn new(
    w0: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 2147483646&gt;</a>,
    w1: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 2147483646&gt;</a>,
    w2: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 2147483646&gt;</a>,
    w3: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 2147483646&gt;</a>,
) -&gt; <a href="core-qm31-qm31.html">qm31</a></code></pre>


### unpack

Returns the parts of the given `qm31` as `m31`s.

Fully qualified path: [core](./core.md)::[qm31](./core-qm31.md)::[QM31Trait](./core-qm31-QM31Trait.md)::[unpack](./core-qm31-QM31Trait.md#unpack)

<pre><code class="language-cairo">fn unpack(self: <a href="core-qm31-qm31.html">qm31</a>) -&gt; BoundedInt&lt;0, 2147483646&gt;; 4]</code></pre>


