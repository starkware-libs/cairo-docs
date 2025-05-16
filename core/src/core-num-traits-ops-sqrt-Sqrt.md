# Sqrt

A trait for computing the square root of a number.  # Examples
```cairo
use core::num::traits::Sqrt;

assert!(9_u8.sqrt() == 3);
```

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt`

<pre><code class="language-rust">pub trait Sqrt&lt;T&gt;</code></pre>

## Trait functions

### sqrt

Computes the square root of a number.

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt::sqrt`

<pre><code class="language-rust">fn sqrt(self: T) -&gt; Self::Target</code></pre>


## Trait types

### Target

The type of the result of the square root operation.

Fully qualified path: `core::num::traits::ops::sqrt::Sqrt::Target`

<pre><code class="language-rust">type Target;</code></pre>


