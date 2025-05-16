# WideMul

A trait for types that can be multiplied together to produce a wider type.This trait enables multiplication operations where the result type has double the bit width of the input types, preventing overflow in cases where the result would exceed the input type's maximum value.  # Examples
```cairo
use core::num::traits::WideMul;

let a: u8 = 255; // maximum value for u8
let b: u8 = 255;
let result: u16 = a.wide_mul(b);
assert!(result == 65025);
```

Fully qualified path: `core::num::traits::ops::widemul::WideMul`

<pre><code class="language-rust">pub trait WideMul&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### wide_mul

Multiply two values together, producing a wider type.

Fully qualified path: `core::num::traits::ops::widemul::WideMul::wide_mul`

<pre><code class="language-rust">fn wide_mul(self: Lhs, other: Rhs) -&gt; Self::Target</code></pre>


## Trait types

### Target

The type of the result of the multiplication.

Fully qualified path: `core::num::traits::ops::widemul::WideMul::Target`

<pre><code class="language-rust">type Target;</code></pre>


