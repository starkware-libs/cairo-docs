# SpanIndex

Fully qualified path: `core::array::SpanIndex`

<pre><code class="language-rust">pub impl SpanIndex&lt;T&gt; of IndexView&lt;Span&lt;T&gt;, usize, @T&gt;</code></pre>

## Impl functions

### index

Returns a snapshot of the element at the given index.  # Examples
```cairo
let span: @Span<u8> = @array![1, 2, 3].span();
let element: @u8 = span[0];
assert!(element == @1);
```

Fully qualified path: `core::array::SpanIndex::index`

<pre><code class="language-rust">fn index(self: @Span&lt;T&gt;, index: usize) -&gt; @T</code></pre>


