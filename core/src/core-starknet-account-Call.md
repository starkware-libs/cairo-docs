# Call

A struct representing a call to a contract.

Fully qualified path: `core::starknet::account::Call`

<pre><code class="language-rust">#[derive(Drop, Copy, Serde, Debug)]
pub struct Call {
    pub to: ContractAddress,
    pub selector: felt252,
    pub calldata: Span&lt;felt252&gt;,
}</code></pre>

## Members

### to

The address of the contract to call.

Fully qualified path: `core::starknet::account::Call::to`

<pre><code class="language-rust">pub to: ContractAddress</code></pre>


### selector

The entry point selector in the called contract.

Fully qualified path: `core::starknet::account::Call::selector`

<pre><code class="language-rust">pub selector: felt252</code></pre>


### calldata

The calldata to pass to entry point.

Fully qualified path: `core::starknet::account::Call::calldata`

<pre><code class="language-rust">pub calldata: Span&lt;felt252&gt;</code></pre>


