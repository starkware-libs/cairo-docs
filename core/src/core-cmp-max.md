# max

Takes two comparable values `a` and `b` and returns the greater of the two values.  # Examples
```cairo
use core::cmp::max;

assert!(max(0, 1) == 1);
```

Fully qualified path: `core::cmp::max`

<pre><code class="language-rust">pub fn max&lt;T, +PartialOrd&lt;T&gt;, +Drop&lt;T&gt;, +Copy&lt;T&gt;&gt;(a: T, b: T) -&gt; T</code></pre>

