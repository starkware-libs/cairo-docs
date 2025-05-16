# DestructWith

Wrapper type to ensure that a type `T` is destructed using a specific `Destruct` impl.

Fully qualified path: `core::internal::DestructWith`

<pre><code class="language-rust">pub struct DestructWith&lt;T, impl DestructT: Destruct&lt;T&gt;&gt; {
    pub value: T,
}</code></pre>

## Members

### value

Fully qualified path: `core::internal::DestructWith::value`

<pre><code class="language-rust">pub value: T</code></pre>


