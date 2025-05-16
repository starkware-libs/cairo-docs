# panic_with_byte_array

Panics with a `ByteArray` message.Constructs a panic message by prepending the `BYTE_ARRAY_MAGIC` value and serializing the provided `ByteArray` into the panic data.  # Examples
```cairo
use core::panics::panic_with_byte_array;

let error_msg = "An error occurred";
panic_with_byte_array(@error_msg);
```

Fully qualified path: `core::panics::panic_with_byte_array`

<pre><code class="language-rust">pub fn panic_with_byte_array(err: @ByteArray) -&gt; crate::never</code></pre>

