# Zero

Defines an additive identity element for `T`.  # Laws
```text
a + 0 = a       ∀ a ∈ T
0 + a = a       ∀ a ∈ T
```

Fully qualified path: `core::num::traits::zero::Zero`

<pre><code class="language-rust">pub trait Zero&lt;T&gt;</code></pre>

## Trait functions

### zero

Returns the additive identity element of `T`, `0`.  # Examples
```cairo
use core::num::traits::Zero;

assert!(Zero::<u32>::zero() == 0);
```

Fully qualified path: `core::num::traits::zero::Zero::zero`

<pre><code class="language-rust">fn zero() -&gt; T</code></pre>


### is_zero

Returns true if `self` is equal to the additive identity.  # Examples
```cairo
use core::num::traits::Zero;

assert!(0.is_zero());
assert!(!5.is_zero());
```

Fully qualified path: `core::num::traits::zero::Zero::is_zero`

<pre><code class="language-rust">fn is_zero(self: @T) -&gt; bool</code></pre>


### is_non_zero

Returns false if `self` is equal to the additive identity.  # Examples
```cairo
use core::num::traits::Zero;

assert!(5.is_non_zero());
assert!(!0.is_non_zero());
```

Fully qualified path: `core::num::traits::zero::Zero::is_non_zero`

<pre><code class="language-rust">fn is_non_zero(self: @T) -&gt; bool</code></pre>


