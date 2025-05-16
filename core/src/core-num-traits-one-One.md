# One

Defines a multiplicative identity element for `T`.  # Laws
```text
a * 1 = a       ∀ a ∈ T
1 * a = a       ∀ a ∈ T
```

Fully qualified path: `core::num::traits::one::One`

<pre><code class="language-rust">pub trait One&lt;T&gt;</code></pre>

## Trait functions

### one

Returns the multiplicative identity element of `T`, `1`.  # Examples
```cairo
use core::num::traits::One;

assert!(One::<u32>::one() == 1);
```

Fully qualified path: `core::num::traits::one::One::one`

<pre><code class="language-rust">fn one() -&gt; T</code></pre>


### is_one

Returns true if `self` is equal to the multiplicative identity.  # Examples
```cairo
use core::num::traits::One;

assert!(1.is_one());
assert!(!0.is_one());
```

Fully qualified path: `core::num::traits::one::One::is_one`

<pre><code class="language-rust">fn is_one(self: @T) -&gt; bool</code></pre>


### is_non_one

Returns false if `self` is equal to the multiplicative identity.  # Examples
```cairo
use core::num::traits::One;

assert!(0.is_non_one());
assert!(!1.is_non_one());
```

Fully qualified path: `core::num::traits::one::One::is_non_one`

<pre><code class="language-rust">fn is_non_one(self: @T) -&gt; bool</code></pre>


