# keccak_syscall

Computes the keccak of the input.The input must be a multiple of 1088 bits (== 17 u64 words) * The input must be pre-padded following the Keccak padding rule (pad10*1): 1. Add a '1' bit 2. Add zero or more '0' bits 3. Add a final '1' bit The total length after padding must be a multiple of 1088 bits  # Arguments`input` - Array of 64-bit words (little endian) to be hashed.  # ReturnsThe keccak hash as a little-endian u256

Fully qualified path: `core::starknet::syscalls::keccak_syscall`

<pre><code class="language-rust">pub extern fn keccak_syscall(
    input: Span&lt;u64&gt;,
) -&gt; SyscallResult&lt;u256&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

