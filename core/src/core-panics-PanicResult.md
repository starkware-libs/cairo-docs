# PanicResult

Result type for operations that can trigger a panic.

Fully qualified path: `core::panics::PanicResult`

<pre><code class="language-rust">pub enum PanicResult&lt;T&gt; {
    Ok: T,
    Err: (Panic, Array&lt;felt252&gt;),
}</code></pre>

## Variants

### Ok

Fully qualified path: `core::panics::PanicResult::Ok`

<pre><code class="language-rust">Ok : T</code></pre>


### Err

Fully qualified path: `core::panics::PanicResult::Err`

<pre><code class="language-rust">Err : ( Panic , Array &lt; felt252 &gt; )</code></pre>


