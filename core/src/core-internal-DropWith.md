# DropWith

Wrapper type to ensure that a type `T` is dropped using a specific `Drop` impl.

Fully qualified path: `core::internal::DropWith`

<pre><code class="language-rust">pub struct DropWith&lt;T, impl DropT: Drop&lt;T&gt;&gt; {
    pub value: T,
}</code></pre>

## Members

### value

Fully qualified path: `core::internal::DropWith::value`

<pre><code class="language-rust">pub value: T</code></pre>


