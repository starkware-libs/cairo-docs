# emit_event_syscall

Emits an event.  # Arguments`keys` - The keys of the event. * `data` - The data of the event.

Fully qualified path: `core::starknet::syscalls::emit_event_syscall`

<pre><code class="language-rust">pub extern fn emit_event_syscall(
    keys: Span&lt;felt252&gt;, data: Span&lt;felt252&gt;,
) -&gt; SyscallResult&lt;()&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

