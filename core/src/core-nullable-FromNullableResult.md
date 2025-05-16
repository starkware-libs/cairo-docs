# FromNullableResult

Represents the result of matching a `Nullable` value.Used to safely handle both null and non-null cases when using `match_nullable` on a `Nullable`.

Fully qualified path: `core::nullable::FromNullableResult`

<pre><code class="language-rust">pub enum FromNullableResult&lt;T&gt; {
    Null,
    NotNull: Box&lt;T&gt;,
}</code></pre>

## Variants

### Null

Represents a null value

Fully qualified path: `core::nullable::FromNullableResult::Null`

<pre><code class="language-rust">Null</code></pre>


### NotNull

The boxed value when not null

Fully qualified path: `core::nullable::FromNullableResult::NotNull`

<pre><code class="language-rust">NotNull : Box &lt; T &gt;</code></pre>


