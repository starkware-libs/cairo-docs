# get_block_info

Returns the block information for the current block.  # Examples
```cairo
use starknet::get_block_info;

let block_info = get_block_info().unbox();

let block_number = block_info.block_number;
let block_timestamp = block_info.block_timestamp;
let sequencer = block_info.sequencer_address;
```

Fully qualified path: `core::starknet::info::get_block_info`

<pre><code class="language-rust">pub fn get_block_info() -&gt; Box&lt;BlockInfo&gt;</code></pre>

