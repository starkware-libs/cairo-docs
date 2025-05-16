# BitSize

A trait used to retrieve the size of a type in bits.

Fully qualified path: `core::num::traits::bit_size::BitSize`

<pre><code class="language-rust">pub trait BitSize&lt;T&gt;</code></pre>

## Trait functions

### bits

Returns the bit size of `T` as a `usize`.  # Examples
```cairo
use core::num::traits::BitSize;

let bits = BitSize::<u8>::bits();
assert!(bits == 8);
```

Fully qualified path: `core::num::traits::bit_size::BitSize::bits`

<pre><code class="language-rust">fn bits() -&gt; usize</code></pre>


