# call_contract_syscall

Calls a given contract.  # Arguments`address` - The address of the called contract. * `entry_point_selector` - A selector for a function within that contract. * `calldata` - Call arguments.

Fully qualified path: `core::starknet::syscalls::call_contract_syscall`

<pre><code class="language-rust">pub extern fn call_contract_syscall(
    address: ContractAddress, entry_point_selector: felt252, calldata: Span&lt;felt252&gt;,
) -&gt; SyscallResult&lt;Span&lt;felt252&gt;&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

