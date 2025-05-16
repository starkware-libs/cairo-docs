# OverflowingSub

Performs subtraction with a flag for overflow.  # Examples
```cairo
use core::num::traits::OverflowingSub;

let (result, is_underflow) = 1_u8.overflowing_sub(2_u8);
assert!(result == 255);
assert!(is_underflow);
```

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingSub`

<pre><code class="language-rust">pub trait OverflowingSub&lt;T&gt;</code></pre>

## Trait functions

### overflowing_sub

Returns a tuple of the difference along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

Fully qualified path: `core::num::traits::ops::overflowing::OverflowingSub::overflowing_sub`

<pre><code class="language-rust">fn overflowing_sub(self: T, v: T) -&gt; (T, bool)</code></pre>


