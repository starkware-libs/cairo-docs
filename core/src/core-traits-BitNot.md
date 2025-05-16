# BitNot

The bitwise NOT operator `~`.  # ExamplesAn implementation of `BitNot` for a wrapper around `u8`.
```cairo
use core::traits::BitNot;

#[derive(Drop, PartialEq)]
struct Wrapper {
    u8: u8,
}

impl BitNotWrapper of BitNot<Wrapper> {
    fn bitnot(a: Wrapper) -> Wrapper {
        Wrapper { u8: ~a.u8 }
    }
}

assert!(~Wrapper { u8: 0 } == Wrapper { u8 : 255 });
assert!(~Wrapper { u8: 1 } == Wrapper { u8 : 254 });
```

Fully qualified path: `core::traits::BitNot`

<pre><code class="language-rust">pub trait BitNot&lt;T&gt;</code></pre>

## Trait functions

### bitnot

Performs the `~` operation.  # Examples
```cairo
assert!(~1_u8 == 254);
```

Fully qualified path: `core::traits::BitNot::bitnot`

<pre><code class="language-rust">fn bitnot(a: T) -&gt; T</code></pre>


