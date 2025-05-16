# storage_base_address_const

Returns a `StorageBaseAddress` given a constant `felt252` value.The value is validated to be in the range `[0, 2**251 - 256)` at compile time.  # Examples
```cairo
use starknet::storage_access::storage_base_address_const;

let base_address = storage_base_address_const::<0>();
```

Fully qualified path: `core::starknet::storage_access::storage_base_address_const`

<pre><code class="language-rust">pub extern fn storage_base_address_const&lt;const address: felt252&gt;() -&gt; StorageBaseAddress nopanic;</code></pre>

