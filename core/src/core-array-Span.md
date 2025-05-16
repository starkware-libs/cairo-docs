# Span

A span is a view into a contiguous collection of the same type - such as `Array`. It is a structure with a single field that holds a snapshot of an array. `Span` implements the `Copy` and the `Drop` traits.

Fully qualified path: `core::array::Span`

<pre><code class="language-rust">pub struct Span&lt;T&gt; {
    pub(crate) snapshot: @Array&lt;T&gt;,
}</code></pre>

