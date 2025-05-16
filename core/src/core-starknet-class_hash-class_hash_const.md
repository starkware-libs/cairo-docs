# class_hash_const

Returns a `ClassHash` given a `felt252` value.  # Examples
```cairo
use starknet::class_hash::class_hash_const;

let class_hash = class_hash_const::<0x123>();
```

Fully qualified path: `core::starknet::class_hash::class_hash_const`

<pre><code class="language-rust">pub extern fn class_hash_const&lt;const address: felt252&gt;() -&gt; ClassHash nopanic;</code></pre>

