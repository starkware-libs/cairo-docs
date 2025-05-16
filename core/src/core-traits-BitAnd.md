# BitAnd

The bitwise AND operator `&`.  # ExamplesAn implementation of `BitAnd` for a wrapper around `bool`.
```cairo
use core::traits::BitAnd;

#[derive(Drop, PartialEq)]
struct Scalar {
    inner: bool,
}

impl BitAndScalar of BitAnd<Scalar> {
    fn bitand(lhs: Scalar, rhs: Scalar) -> Scalar {
       Scalar { inner: lhs.inner & rhs.inner }
    }
}

assert!(Scalar { inner: true } & Scalar { inner: true } == Scalar { inner: true });
assert!(Scalar { inner: true } & Scalar { inner: false } == Scalar { inner: false });
assert!(Scalar { inner: false } & Scalar { inner: true } == Scalar { inner: false });
assert!(Scalar { inner: false } & Scalar { inner: false } == Scalar { inner: false });
```

Fully qualified path: `core::traits::BitAnd`

<pre><code class="language-rust">pub trait BitAnd&lt;T&gt;</code></pre>

## Trait functions

### bitand

Performs the `&` operation.  # Examples
```cairo
assert_eq!(true & false, false);
assert_eq!(5_u8 & 1_u8, 1);
assert_eq!(true & true, true);
assert_eq!(5_u8 & 2_u8, 0);
```

Fully qualified path: `core::traits::BitAnd::bitand`

<pre><code class="language-rust">fn bitand(lhs: T, rhs: T) -&gt; T</code></pre>


