# get_block_hash_syscall

Returns the hash of the block with the given number.  # Arguments`block_number` - The number of the queried block.  # ReturnsThe hash of the block with the given number.

Fully qualified path: `core::starknet::syscalls::get_block_hash_syscall`

<pre><code class="language-rust">pub extern fn get_block_hash_syscall(
    block_number: u64,
) -&gt; SyscallResult&lt;felt252&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

