# FormatAsByteArray

A trait for formatting values into their ASCII string representation in a `ByteArray`.

Fully qualified path: `core::to_byte_array::FormatAsByteArray`

<pre><code class="language-rust">pub trait FormatAsByteArray&lt;T&gt;</code></pre>

## Trait functions

### format_as_byte_array

Returns a new `ByteArray` containing the ASCII representation of the value.  # Examples
```cairo
use core::to_byte_array::FormatAsByteArray;

let num: u32 = 42;
let formatted = num.format_as_byte_array(16);
assert!(formatted, "2a");
```

Fully qualified path: `core::to_byte_array::FormatAsByteArray::format_as_byte_array`

<pre><code class="language-rust">fn format_as_byte_array(self: @T, base: NonZero&lt;T&gt;) -&gt; ByteArray</code></pre>


