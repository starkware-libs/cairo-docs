# contract_address_const

Returns a `ContractAddress` given a `felt252` value.  # Examples
```cairo
use starknet::contract_address::contract_address_const;

let contract_address = contract_address_const::<0x0>();
```

Fully qualified path: `core::starknet::contract_address::contract_address_const`

<pre><code class="language-rust">pub extern fn contract_address_const&lt;const address: felt252&gt;() -&gt; ContractAddress nopanic;</code></pre>

