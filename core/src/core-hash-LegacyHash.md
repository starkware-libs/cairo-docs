# LegacyHash

A trait for hashing values using a `felt252` as hash state, used for backwards compatibility. NOTE: Implement `Hash` instead of this trait if possible.

Fully qualified path: `core::hash::LegacyHash`

<pre><code class="language-rust">pub trait LegacyHash&lt;T&gt;</code></pre>

## Trait functions

### hash

Takes a `felt252` state and a value of type `T` and returns the hash result.  # Examples
```cairo
use core::pedersen::PedersenTrait;
use core::hash::LegacyHash;

let hash = LegacyHash::hash(0, 1);
```

Fully qualified path: `core::hash::LegacyHash::hash`

<pre><code class="language-rust">fn hash(state: felt252, value: T) -&gt; felt252</code></pre>


