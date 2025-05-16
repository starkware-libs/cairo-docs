# set_signature

Set the transaction signature.  # Arguments`signature` - The signature to set.After a call to `set_signature`, `starknet::get_execution_info().tx_info.signature` will return the set value.

Fully qualified path: `core::starknet::testing::set_signature`

<pre><code class="language-rust">pub fn set_signature(signature: Span&lt;felt252&gt;)</code></pre>

