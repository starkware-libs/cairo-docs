# set_account_contract_address

Sets the account contract address.  # Arguments`address` - The account contract to set.After a call to `set_account_contract_address`, `starknet::get_execution_info().tx_info.account_contract_address` will return the set value.

Fully qualified path: `core::starknet::testing::set_account_contract_address`

<pre><code class="language-rust">pub fn set_account_contract_address(address: ContractAddress)</code></pre>

