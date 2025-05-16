# sha256_process_block_syscall

Computes the next SHA-256 state of the input with the given state.  # Arguments`state` - The current SHA-256 state. * `input` - The input provided to compute the next SHA-256 state.  # ReturnsThe next SHA-256 state of the input with the givens state.The system call does not add any padding and the input needs to be a multiple of 512 bits (== 16 u32 word).

Fully qualified path: `core::starknet::syscalls::sha256_process_block_syscall`

<pre><code class="language-rust">pub extern fn sha256_process_block_syscall(
    state: core::sha256::Sha256StateHandle, input: Box&lt;[u32; 16]&gt;,
) -&gt; SyscallResult&lt;core::sha256::Sha256StateHandle&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

