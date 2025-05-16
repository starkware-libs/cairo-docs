# DivAssign

The division assignment operator `/=`.

Fully qualified path: `core::ops::arith::DivAssign`

<pre><code class="language-rust">pub trait DivAssign&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### div_assign

Performs the `/=` operation.  # Examples
```cairo
let mut x: u8 = 3;
x /= x;
assert!(x == 1);
```

Fully qualified path: `core::ops::arith::DivAssign::div_assign`

<pre><code class="language-rust">fn div_assign(ref self: Lhs, rhs: Rhs)</code></pre>


