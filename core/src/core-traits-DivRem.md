# DivRem

Performs truncated division and remainder.This trait provides a way to efficiently compute both the quotient and remainder in a single operation. The division truncates towards zero, matching the behavior of the `/` and `%` operators.  # Examples
```cairo
assert!(DivRem::div_rem(7_u32, 3) == (2, 1));
```

Fully qualified path: `core::traits::DivRem`

<pre><code class="language-rust">pub trait DivRem&lt;T&gt;</code></pre>

## Trait functions

### div_rem

Performs the `/` and the `%` operations, returning both the quotient and remainder.  # Examples
```cairo
assert!(DivRem::div_rem(12_u32, 10) == (1, 2));
```

Fully qualified path: `core::traits::DivRem::div_rem`

<pre><code class="language-rust">fn div_rem(lhs: T, rhs: NonZero&lt;T&gt;) -&gt; (T, T)</code></pre>


