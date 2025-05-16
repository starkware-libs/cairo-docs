# panic

Triggers an immediate panic with the provided data and terminates execution.  # Examples
```cairo
use core::panics::panic;

panic(array!['An error occurred']);
```

Fully qualified path: `core::panics::panic`

<pre><code class="language-rust">pub extern fn panic(data: Array&lt;felt252&gt;) -&gt; crate::never;</code></pre>

