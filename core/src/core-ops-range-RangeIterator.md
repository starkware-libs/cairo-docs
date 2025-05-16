# RangeIterator

Represents an iterator located at `cur`, whose end is `end` (`cur <= end`).

Fully qualified path: `core::ops::range::RangeIterator`

<pre><code class="language-rust">#[derive(Clone, Drop, PartialEq)]
pub struct RangeIterator&lt;T&gt; {
    cur: T,
    end: T,
}</code></pre>

