# WrappingSub

Performs subtraction that wraps around on overflow.  # Examples
```cairo
use core::num::traits::WrappingSub;

let result = 0_u8.wrapping_sub(1);
assert!(result == 255);

let result = 100_u8.wrapping_sub(150);
assert!(result == 206);
```

Fully qualified path: `core::num::traits::ops::wrapping::WrappingSub`

<pre><code class="language-rust">pub trait WrappingSub&lt;T&gt;</code></pre>

## Trait functions

### wrapping_sub

Wrapping (modular) subtraction. Computes `self - other`, wrapping around at the boundary of the type.

Fully qualified path: `core::num::traits::ops::wrapping::WrappingSub::wrapping_sub`

<pre><code class="language-rust">fn wrapping_sub(self: T, v: T) -&gt; T</code></pre>


