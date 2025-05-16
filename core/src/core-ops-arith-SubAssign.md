# SubAssign

The subtraction assignment operator `-=`.

Fully qualified path: `core::ops::arith::SubAssign`

<pre><code class="language-rust">pub trait SubAssign&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### sub_assign

Performs the `-=` operation.  # Examples
```cairo
let mut x: u8 = 3;
x -= x;
assert!(x == 0);
```

Fully qualified path: `core::ops::arith::SubAssign::sub_assign`

<pre><code class="language-rust">fn sub_assign(ref self: Lhs, rhs: Rhs)</code></pre>


