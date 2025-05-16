# PoseidonImpl

A trait for creating a new Poseidon hash state.

Fully qualified path: `core::poseidon::PoseidonImpl`

<pre><code class="language-rust">pub impl PoseidonImpl of PoseidonTrait</code></pre>

## Impl functions

### new

Creates an initial state with all fields set to 0.  # Examples
```cairo
use core::poseidon::PoseidonTrait;

let mut state = PoseidonTrait::new();
```

Fully qualified path: `core::poseidon::PoseidonImpl::new`

<pre><code class="language-rust">fn new() -&gt; HashState</code></pre>


