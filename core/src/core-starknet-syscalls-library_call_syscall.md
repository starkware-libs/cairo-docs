# library_call_syscall

Calls the requested function in any previously declared class.  # Arguments`class_hash` - The hash of the class to be used. * `function_selector` - A selector for a function within that class. * `calldata` - Call arguments.

Fully qualified path: `core::starknet::syscalls::library_call_syscall`

<pre><code class="language-rust">pub extern fn library_call_syscall(
    class_hash: ClassHash, function_selector: felt252, calldata: Span&lt;felt252&gt;,
) -&gt; SyscallResult&lt;Span&lt;felt252&gt;&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

