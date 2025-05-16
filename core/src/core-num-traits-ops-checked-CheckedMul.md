# CheckedMul

Performs multiplication that returns `None` instead of wrapping around on underflow or overflow.  # Examples
```cairo
use core::num::traits::CheckedMul;

let result = 10_u8.checked_mul(20);
assert!(result == Some(200));

let result = 10_u8.checked_mul(30);
assert!(result == None); // Overflow
```

Fully qualified path: `core::num::traits::ops::checked::CheckedMul`

<pre><code class="language-rust">pub trait CheckedMul&lt;T&gt;</code></pre>

## Trait functions

### checked_mul

Multiplies two numbers, checking for underflow or overflow. If underflow or overflow happens, `None` is returned.

Fully qualified path: `core::num::traits::ops::checked::CheckedMul::checked_mul`

<pre><code class="language-rust">fn checked_mul(self: T, v: T) -&gt; Option&lt;T&gt;</code></pre>


