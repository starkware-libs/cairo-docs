# RemAssign

The remainder assignment operator `%=`.

Fully qualified path: `core::ops::arith::RemAssign`

<pre><code class="language-rust">pub trait RemAssign&lt;Lhs, Rhs&gt;</code></pre>

## Trait functions

### rem_assign

Performs the `%=` operation.  # Examples
```cairo
let mut x: u8 = 3;
x %= x;
assert!(x == 0);
```

Fully qualified path: `core::ops::arith::RemAssign::rem_assign`

<pre><code class="language-rust">fn rem_assign(ref self: Lhs, rhs: Rhs)</code></pre>


