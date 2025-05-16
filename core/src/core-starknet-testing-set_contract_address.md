# set_contract_address

Sets the contract address to the provided value.  # Arguments`address` - The contract address to set.After a call to `set_contract_address`, `starknet::get_execution_info().contract_address` will return the set value.

Fully qualified path: `core::starknet::testing::set_contract_address`

<pre><code class="language-rust">pub fn set_contract_address(address: ContractAddress)</code></pre>

