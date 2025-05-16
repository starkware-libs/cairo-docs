# Range

A (half-open) range bounded inclusively below and exclusively above (`start..end`).The range `start..end` contains all values with `start <= x < end`. It is empty if `start >= end`.  # ExamplesThe `start..end` syntax is a `Range`:
```cairo
assert!((3..5) == core::ops::Range { start: 3, end: 5 });

let mut sum = 0;
for i in 3..6 {
    sum += i;
}
assert!(sum == 3 + 4 + 5);
```

Fully qualified path: `core::ops::range::Range`

<pre><code class="language-rust">#[derive(Clone, Drop, PartialEq)]
pub struct Range&lt;T&gt; {
    pub start: T,
    pub end: T,
}</code></pre>

## Members

### start

The lower bound of the range (inclusive).

Fully qualified path: `core::ops::range::Range::start`

<pre><code class="language-rust">pub start: T</code></pre>


### end

The upper bound of the range (exclusive).

Fully qualified path: `core::ops::range::Range::end`

<pre><code class="language-rust">pub end: T</code></pre>


