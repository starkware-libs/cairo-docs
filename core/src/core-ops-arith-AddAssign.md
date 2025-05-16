# AddAssign

The addition assignment operator `+=`.

Fully qualified path: `core::ops::arith::AddAssign`

<pre><code class="language-rust">pub trait AddAssign&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### add_assign

Performs the `+=` operation.  # Examples
```cairo
let mut x: u8 = 3;
x += x;
assert!(x == 6);
```

Fully qualified path: `core::ops::arith::AddAssign::add_assign`

<pre><code class="language-rust">fn add_assign(ref self: Lhs, rhs: Rhs)</code></pre>


