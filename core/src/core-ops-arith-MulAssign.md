# MulAssign

The multiplication assignment operator `*=`.

Fully qualified path: `core::ops::arith::MulAssign`

<pre><code class="language-rust">pub trait MulAssign&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### mul_assign

Performs the `*=` operation.  # Examples
```cairo
let mut x: u8 = 3;
x *= x;
assert!(x == 9);
```

Fully qualified path: `core::ops::arith::MulAssign::mul_assign`

<pre><code class="language-rust">fn mul_assign(ref self: Lhs, rhs: Rhs)</code></pre>


