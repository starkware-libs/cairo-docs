# TxInfo

Extended information about the current transaction.

Fully qualified path: `core::starknet::info::v2::TxInfo`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug, Serde)]
pub struct TxInfo {
    pub version: felt252,
    pub account_contract_address: ContractAddress,
    pub max_fee: u128,
    pub signature: Span&lt;felt252&gt;,
    pub transaction_hash: felt252,
    pub chain_id: felt252,
    pub nonce: felt252,
    pub resource_bounds: Span&lt;ResourceBounds&gt;,
    pub tip: u128,
    pub paymaster_data: Span&lt;felt252&gt;,
    pub nonce_data_availability_mode: u32,
    pub fee_data_availability_mode: u32,
    pub account_deployment_data: Span&lt;felt252&gt;,
}</code></pre>

## Members

### version

The version of the transaction. It is fixed (currently, 1) in the OS, and should be signed by the account contract. This field allows invalidating old transactions, whenever the meaning of the other transaction fields is changed (in the OS).

Fully qualified path: `core::starknet::info::v2::TxInfo::version`

<pre><code class="language-rust">pub version: felt252</code></pre>


### account_contract_address

The account contract from which this transaction originates.

Fully qualified path: `core::starknet::info::v2::TxInfo::account_contract_address`

<pre><code class="language-rust">pub account_contract_address: ContractAddress</code></pre>


### max_fee

The `max_fee` field of the transaction.

Fully qualified path: `core::starknet::info::v2::TxInfo::max_fee`

<pre><code class="language-rust">pub max_fee: u128</code></pre>


### signature

The signature of the transaction.

Fully qualified path: `core::starknet::info::v2::TxInfo::signature`

<pre><code class="language-rust">pub signature: Span&lt;felt252&gt;</code></pre>


### transaction_hash

The hash of the transaction.

Fully qualified path: `core::starknet::info::v2::TxInfo::transaction_hash`

<pre><code class="language-rust">pub transaction_hash: felt252</code></pre>


### chain_id

The identifier of the chain. This field can be used to prevent replay of testnet transactions on mainnet.

Fully qualified path: `core::starknet::info::v2::TxInfo::chain_id`

<pre><code class="language-rust">pub chain_id: felt252</code></pre>


### nonce

The transaction's nonce.

Fully qualified path: `core::starknet::info::v2::TxInfo::nonce`

<pre><code class="language-rust">pub nonce: felt252</code></pre>


### resource_bounds

A span of `ResourceBounds` structs used for V3 transactions.

Fully qualified path: `core::starknet::info::v2::TxInfo::resource_bounds`

<pre><code class="language-rust">pub resource_bounds: Span&lt;ResourceBounds&gt;</code></pre>


### tip

The tip of the transaction.

Fully qualified path: `core::starknet::info::v2::TxInfo::tip`

<pre><code class="language-rust">pub tip: u128</code></pre>


### paymaster_data

If specified, the paymaster should pay for the execution of the transaction. The data includes the address of the paymaster sponsoring the transaction, followed by extra data to send to the paymaster. Used for V3 transactions.

Fully qualified path: `core::starknet::info::v2::TxInfo::paymaster_data`

<pre><code class="language-rust">pub paymaster_data: Span&lt;felt252&gt;</code></pre>


### nonce_data_availability_mode

The data availability mode for the nonce. Used for V3 transactions.

Fully qualified path: `core::starknet::info::v2::TxInfo::nonce_data_availability_mode`

<pre><code class="language-rust">pub nonce_data_availability_mode: u32</code></pre>


### fee_data_availability_mode

The data availability mode for the account balance from which fee will be taken. Used for V3 transactions.

Fully qualified path: `core::starknet::info::v2::TxInfo::fee_data_availability_mode`

<pre><code class="language-rust">pub fee_data_availability_mode: u32</code></pre>


### account_deployment_data

If nonempty, will contain the required data for deploying and initializing an account contract: its class hash, address salt and constructor calldata. Used for V3 transactions.

Fully qualified path: `core::starknet::info::v2::TxInfo::account_deployment_data`

<pre><code class="language-rust">pub account_deployment_data: Span&lt;felt252&gt;</code></pre>


