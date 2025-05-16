# Rem

The remainder operator `%`.Types implementing this trait support the remainder operation via the `%` operator.  # Examples
```cairo
assert!(3_u8 % 2_u8 == 1_u8);
```

Fully qualified path: `core::traits::Rem`

<pre><code class="language-rust">pub trait Rem&lt;T&gt;</code></pre>

## Trait functions

### rem

Performs the `%` operation.  # Examples
```cairo
assert!(12_u8 % 10_u8 == 2_u8);
```

Fully qualified path: `core::traits::Rem::rem`

<pre><code class="language-rust">fn rem(lhs: T, rhs: T) -&gt; T</code></pre>


