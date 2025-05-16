# Clone

A common trait for the ability to explicitly duplicate an object.Differs from `Copy` in that `Copy` is implicit and inexpensive, while `Clone` is always explicit and may or may not be expensive.Since `Clone` is more general than `Copy`, you can automatically make anything `Copy` be `Clone` as well.  ## DerivableThis trait can be used with `#[derive]` if all fields are `Clone`. The `derive`d implementation of `Clone` calls `clone` on each field.

Fully qualified path: `core::clone::Clone`

<pre><code class="language-rust">pub trait Clone&lt;T&gt;</code></pre>

## Trait functions

### clone

Returns a copy of the value.  # Examples
```cairo
let arr = array![1, 2, 3];
assert!(arr == arr.clone());
```

Fully qualified path: `core::clone::Clone::clone`

<pre><code class="language-rust">fn clone(self: @T) -&gt; T</code></pre>


