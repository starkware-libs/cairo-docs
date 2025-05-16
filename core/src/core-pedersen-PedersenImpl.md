# PedersenImpl

A trait for creating a new Pedersen hash state.

Fully qualified path: `core::pedersen::PedersenImpl`

<pre><code class="language-rust">pub impl PedersenImpl of PedersenTrait</code></pre>

## Impl functions

### new

Creates a new Pedersen hash state with the given base value.  # Examples
```cairo
use core::pedersen::PedersenTrait;

let mut state = PedersenTrait::new(0);
assert!(state.state == 0);
```

Fully qualified path: `core::pedersen::PedersenImpl::new`

<pre><code class="language-rust">fn new(base: felt252) -&gt; HashState</code></pre>


