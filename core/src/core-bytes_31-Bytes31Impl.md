# Bytes31Impl

A trait for accessing a specific byte of a `bytes31` type.

Fully qualified path: `core::bytes_31::Bytes31Impl`

<pre><code class="language-rust">pub impl Bytes31Impl of Bytes31Trait</code></pre>

## Impl functions

### at

Returns the byte at the given index (LSB's index is 0).Assumes that `index < BYTES_IN_BYTES31`. If the assumption is not met, the behavior is undefined.  # Examples
```cairo
let bytes: bytes31 = 1_u8.into();
assert!(bytes.at(0) == 1);
```

Fully qualified path: `core::bytes_31::Bytes31Impl::at`

<pre><code class="language-rust">fn at(self: @bytes31, index: usize) -&gt; u8</code></pre>


