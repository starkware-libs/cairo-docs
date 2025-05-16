# send_message_to_l1_syscall

Sends a message to L1.  # Arguments`to_address` - The recipient's L1 address. * `payload` - The content of the message.

Fully qualified path: `core::starknet::syscalls::send_message_to_l1_syscall`

<pre><code class="language-rust">pub extern fn send_message_to_l1_syscall(
    to_address: felt252, payload: Span&lt;felt252&gt;,
) -&gt; SyscallResult&lt;()&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

