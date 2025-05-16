# HashState

Represents the current state of a Pedersen hash computation.The state is maintained as a single `felt252` value, which is updated through the [`HashStateTrait::finalize`](`HashStateTrait::finalize`) method.

Fully qualified path: `core::pedersen::HashState`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug)]
pub struct HashState {
    pub state: felt252,
}</code></pre>

## Members

### state

The current hash state

Fully qualified path: `core::pedersen::HashState::state`

<pre><code class="language-rust">pub state: felt252</code></pre>


