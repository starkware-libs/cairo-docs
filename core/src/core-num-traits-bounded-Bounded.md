# Bounded

A trait defining minimum and maximum bounds for numeric types.This trait only supports types that can have constant values.

Fully qualified path: `core::num::traits::bounded::Bounded`

<pre><code class="language-rust">pub trait Bounded&lt;T&gt;</code></pre>

## Trait constants

### MIN

Returns the minimum value for type `T`.  # Examples
```cairo
use core::num::traits::Bounded;

let min = Bounded::<u8>::MIN;
assert!(min == 0);
```

Fully qualified path: `core::num::traits::bounded::Bounded::MIN`

<pre><code class="language-rust">const MIN: T;</code></pre>


### MAX

Returns the maximum value for type `T`.  # Examples
```cairo
use core::num::traits::Bounded;

let max = Bounded::<u8>::MAX;
assert!(max == 255);
```

Fully qualified path: `core::num::traits::bounded::Bounded::MAX`

<pre><code class="language-rust">const MAX: T;</code></pre>


