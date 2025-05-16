# CheckedAdd

Performs addition that returns `None` instead of wrapping around on overflow.  # Examples
```cairo
use core::num::traits::CheckedAdd;

let result = 1_u8.checked_add(2);
assert!(result == Some(3));

let result = 255_u8.checked_add(1);
assert!(result == None); // Overflow
```

Fully qualified path: `core::num::traits::ops::checked::CheckedAdd`

<pre><code class="language-rust">pub trait CheckedAdd&lt;T&gt;</code></pre>

## Trait functions

### checked_add

Adds two numbers, checking for overflow. If overflow happens, `None` is returned.

Fully qualified path: `core::num::traits::ops::checked::CheckedAdd::checked_add`

<pre><code class="language-rust">fn checked_add(self: T, v: T) -&gt; Option&lt;T&gt;</code></pre>


