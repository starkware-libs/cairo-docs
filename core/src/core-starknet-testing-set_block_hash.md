# set_block_hash

Set the hash for a block.  # Arguments`block_number` - The targeted block number. `value` - The block hash to set.After a call to `set_block_hash`, `starknet::syscalls::get_block_hash_syscall` for the block_number will return the set value. Unset blocks values call would fail.

Fully qualified path: `core::starknet::testing::set_block_hash`

<pre><code class="language-rust">pub fn set_block_hash(block_number: u64, value: felt252)</code></pre>

