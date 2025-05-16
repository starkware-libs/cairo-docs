# Pow

Raises a value to the power of `exp`.Note that `0⁰` (`pow(0, 0)`) returns `1`. Mathematically this is undefined.  # PanicsPanics if the result of the exponentiation operation overflows the output type.  # Examples
```cairo
use core::num::traits::Pow;

assert!(2_i8.pow(4_usize) == 16_i8);
assert!(6_u8.pow(3_usize) == 216_u8);
assert!(0_u8.pow(0_usize) == 1_u8);
```

Fully qualified path: `core::num::traits::ops::pow::Pow`

<pre><code class="language-rust">pub trait Pow&lt;Base, Exp&gt;</code></pre>

## Trait functions

### pow

Returns `self` to the power `exp`.

Fully qualified path: `core::num::traits::ops::pow::Pow::pow`

<pre><code class="language-rust">fn pow(self: Base, exp: Exp) -&gt; Self::Output</code></pre>


## Trait types

### Output

The type of the result of the power calculation.

Fully qualified path: `core::num::traits::ops::pow::Pow::Output`

<pre><code class="language-rust">type Output;</code></pre>


