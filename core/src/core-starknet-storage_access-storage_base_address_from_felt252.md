# storage_base_address_from_felt252

Returns a `StorageBaseAddress` given a `felt252` value.Wraps around the value if it is not in the range `[0, 2**251 - 256)`.

Fully qualified path: `core::starknet::storage_access::storage_base_address_from_felt252`

<pre><code class="language-rust">pub extern fn storage_base_address_from_felt252(
    addr: felt252,
) -&gt; StorageBaseAddress implicits(RangeCheck) nopanic;</code></pre>

