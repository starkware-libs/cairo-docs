# PedersenTrait

Fully qualified path: `core::pedersen::PedersenTrait`

<pre><code class="language-rust">pub trait PedersenTrait</code></pre>

## Trait functions

### new

Creates a new Pedersen hash state with the given base value.  # Examples
```cairo
use core::pedersen::PedersenTrait;

let mut state = PedersenTrait::new(0);
assert!(state.state == 0);
```

Fully qualified path: `core::pedersen::PedersenTrait::new`

<pre><code class="language-rust">fn new(base: felt252) -&gt; HashState</code></pre>


