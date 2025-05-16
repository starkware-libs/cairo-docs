# replace_class_syscall

Replaces the class hash of the current contract, instantly modifying its entrypoints.The new class becomes effective only after the current function call completes. The remaining code in the current function will continue executing from the old class. The new class will be used: * In subsequent transactions * If the contract is called via `call_contract` syscall later in the same transaction  # Arguments`class_hash` - The class hash that should replace the current one.

Fully qualified path: `core::starknet::syscalls::replace_class_syscall`

<pre><code class="language-rust">pub extern fn replace_class_syscall(
    class_hash: ClassHash,
) -&gt; SyscallResult&lt;()&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

