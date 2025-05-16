# Hash

A trait for values that can be hashed.This trait should be implemented for any type that can be included in a hash calculation. The most common way to implement this trait is by using `#[derive(Hash)]`.

Fully qualified path: `core::hash::Hash`

<pre><code class="language-rust">pub trait Hash&lt;T, S, +HashStateTrait&lt;S&gt;&gt;</code></pre>

## Trait functions

### update_state

Updates the hash state with the given value and returns a new hash state.  # Examples
```cairo
use core::pedersen::PedersenTrait;
use core::hash::Hash;

let mut state = PedersenTrait::new(0);
let new_state = Hash::update_state(state, 1);
```

Fully qualified path: `core::hash::Hash::update_state`

<pre><code class="language-rust">fn update_state(state: S, value: T) -&gt; S</code></pre>


