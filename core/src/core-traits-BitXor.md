# BitXor

The bitwise XOR operator `^`.  # ExamplesAn implementation of `BitXor` for a wrapper around `bool`.
```cairo
use core::traits::BitXor;

#[derive(Drop, PartialEq)]
struct Scalar {
    inner: bool,
}

impl BitXorScalar of BitXor<Scalar> {
    fn bitxor(lhs: Scalar, rhs: Scalar) -> Scalar {
        Scalar { inner: lhs.inner ^ rhs.inner }
    }
}

assert!(Scalar { inner: true } ^ Scalar { inner: true } == Scalar { inner: false });
assert!(Scalar { inner: true } ^ Scalar { inner: false } == Scalar { inner: true });
assert!(Scalar { inner: false } ^ Scalar { inner: true } == Scalar { inner: true });
assert!(Scalar { inner: false } ^ Scalar { inner: false } == Scalar { inner: false });
```

Fully qualified path: `core::traits::BitXor`

<pre><code class="language-rust">pub trait BitXor&lt;T&gt;</code></pre>

## Trait functions

### bitxor

Performs the `^` operation.  # Examples
```cairo
assert!(1_u8 ^ 2_u8 == 3);
```

Fully qualified path: `core::traits::BitXor::bitxor`

<pre><code class="language-rust">fn bitxor(lhs: T, rhs: T) -&gt; T</code></pre>


