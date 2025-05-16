# min

Takes two comparable values `a` and `b` and returns the smaller of the two values.  # Examples
```cairo
use core::cmp::min;

assert!(min(0, 1) == 0);
```

Fully qualified path: `core::cmp::min`

<pre><code class="language-rust">pub fn min&lt;T, +PartialOrd&lt;T&gt;, +Drop&lt;T&gt;, +Copy&lt;T&gt;&gt;(a: T, b: T) -&gt; T</code></pre>

