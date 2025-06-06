# sha256_process_block_syscall

Computes the next SHA-256 state of the input with the given state.
# Arguments

- `state` - The current SHA-256 state.
- `input` - The input provided to compute the next SHA-256 state.
# Returns

- The next SHA-256 state of the input with the givens state.

The system call does not add any padding and the input needs to be a multiple of 512 bits
(== 16 u32 word).

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[syscalls](./core-starknet-syscalls.md)::[sha256_process_block_syscall](./core-starknet-syscalls-sha256_process_block_syscall.md)

<pre><code class="language-cairo">pub extern fn sha256_process_block_syscall(state: <a href="core-sha256-Sha256StateHandle.html">Sha256StateHandle</a>, input: <a href="core-box-Box.html">Box&lt;u32; 16]&gt;</a>) -&gt; <a href="core-result-Result.html">Result&lt;Sha256StateHandle, Array&lt;felt252&gt;&gt;</a> implicits(GasBuiltin, System) nopanic;</code></pre>

