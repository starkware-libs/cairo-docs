# BitOr

The bitwise OR operator `|`.  # ExamplesAn implementation of `BitOr` for a wrapper around `bool`.
```cairo
use core::traits::BitOr;

#[derive(Drop, PartialEq)]
struct Scalar {
    inner: bool,
}

impl BitOrScalar of BitOr<Scalar> {
    fn bitor(lhs: Scalar, rhs: Scalar) -> Scalar {
        Scalar { inner: lhs.inner | rhs.inner }
    }
}

assert!(Scalar { inner: true } | Scalar { inner: true } == Scalar { inner: true });
assert!(Scalar { inner: true } | Scalar { inner: false } == Scalar { inner: true });
assert!(Scalar { inner: false } | Scalar { inner: true } == Scalar { inner: true });
assert!(Scalar { inner: false } | Scalar { inner: false } == Scalar { inner: false });
```

Fully qualified path: `core::traits::BitOr`

<pre><code class="language-rust">pub trait BitOr&lt;T&gt;</code></pre>

## Trait functions

### bitor

Performs the `|` operation.  # Examples
```cairo
assert!(1_u8 | 2_u8 == 3);
```

Fully qualified path: `core::traits::BitOr::bitor`

<pre><code class="language-rust">fn bitor(lhs: T, rhs: T) -&gt; T</code></pre>


