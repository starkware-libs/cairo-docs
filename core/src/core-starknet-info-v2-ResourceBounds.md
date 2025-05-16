# ResourceBounds

V3 transactions resources used for enabling the fee market.

Fully qualified path: `core::starknet::info::v2::ResourceBounds`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug, Serde)]
pub struct ResourceBounds {
    pub resource: felt252,
    pub max_amount: u64,
    pub max_price_per_unit: u128,
}</code></pre>

## Members

### resource

The name of the resource.

Fully qualified path: `core::starknet::info::v2::ResourceBounds::resource`

<pre><code class="language-rust">pub resource: felt252</code></pre>


### max_amount

The maximum amount of the resource allowed for usage during the execution.

Fully qualified path: `core::starknet::info::v2::ResourceBounds::max_amount`

<pre><code class="language-rust">pub max_amount: u64</code></pre>


### max_price_per_unit

The maximum price the user is willing to pay for the resource unit.

Fully qualified path: `core::starknet::info::v2::ResourceBounds::max_price_per_unit`

<pre><code class="language-rust">pub max_price_per_unit: u128</code></pre>


