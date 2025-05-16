# set_nonce

Set the transaction nonce.  # Arguments`non` - The nonce to set.After a call to `set_nonce`, `starknet::get_execution_info().tx_info.nonce` will return the set value.

Fully qualified path: `core::starknet::testing::set_nonce`

<pre><code class="language-rust">pub fn set_nonce(nonce: felt252)</code></pre>

