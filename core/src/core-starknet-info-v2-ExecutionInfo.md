# ExecutionInfo

The same as `ExecutionInfo`, but with the `TxInfo` field replaced with `v2::TxInfo`.

Fully qualified path: `core::starknet::info::v2::ExecutionInfo`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug)]
pub struct ExecutionInfo {
    pub block_info: Box&lt;BlockInfo&gt;,
    pub tx_info: Box&lt;TxInfo&gt;,
    pub caller_address: ContractAddress,
    pub contract_address: ContractAddress,
    pub entry_point_selector: felt252,
}</code></pre>

## Members

### block_info

Fully qualified path: `core::starknet::info::v2::ExecutionInfo::block_info`

<pre><code class="language-rust">pub block_info: Box&lt;BlockInfo&gt;</code></pre>


### tx_info

Fully qualified path: `core::starknet::info::v2::ExecutionInfo::tx_info`

<pre><code class="language-rust">pub tx_info: Box&lt;TxInfo&gt;</code></pre>


### caller_address

Fully qualified path: `core::starknet::info::v2::ExecutionInfo::caller_address`

<pre><code class="language-rust">pub caller_address: ContractAddress</code></pre>


### contract_address

Fully qualified path: `core::starknet::info::v2::ExecutionInfo::contract_address`

<pre><code class="language-rust">pub contract_address: ContractAddress</code></pre>


### entry_point_selector

Fully qualified path: `core::starknet::info::v2::ExecutionInfo::entry_point_selector`

<pre><code class="language-rust">pub entry_point_selector: felt252</code></pre>


