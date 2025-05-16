# Result

The type used for returning and propagating errors. It is an enum with the variants `Ok: T`, representing success and containing a value, and `Err: E`, representing error and containing an error value.

Fully qualified path: `core::result::Result`

<pre><code class="language-rust">#[must_use]
#[derive(Copy, Drop, Debug, Serde, PartialEq)]
pub enum Result&lt;T, E&gt; {
    Ok: T,
    Err: E,
}</code></pre>

## Variants

### Ok

Fully qualified path: `core::result::Result::Ok`

<pre><code class="language-rust">Ok : T</code></pre>


### Err

Fully qualified path: `core::result::Result::Err`

<pre><code class="language-rust">Err : E</code></pre>


