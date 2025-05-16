# HashStateTrait

A trait for hash state accumulators.Provides methods to update a hash state with new values and finalize it into a hash result.

Fully qualified path: `core::hash::HashStateTrait`

<pre><code class="language-rust">pub trait HashStateTrait&lt;S&gt;</code></pre>

## Trait functions

### update

Updates the current hash state `self` with the given `felt252` value and returns a new hash state.  # Examples
```cairo
use core::pedersen::PedersenTrait;
use core::hash::HashStateTrait;

let mut state = PedersenTrait::new(0);
state = state.update(1);
```

Fully qualified path: `core::hash::HashStateTrait::update`

<pre><code class="language-rust">fn update(self: S, value: felt252) -&gt; S</code></pre>


### finalize

Takes the current state `self` and returns the hash result.  # Examples
```cairo
use core::pedersen::PedersenTrait;
use core::hash::HashStateTrait;

let mut state = PedersenTrait::new(0);
let hash = state.finalize();
```

Fully qualified path: `core::hash::HashStateTrait::finalize`

<pre><code class="language-rust">fn finalize(self: S) -&gt; felt252</code></pre>


