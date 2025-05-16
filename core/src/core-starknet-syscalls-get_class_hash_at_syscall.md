# get_class_hash_at_syscall

Gets the class hash of the contract at the given address.  # Arguments`contract_address` - The address of the deployed contract.  # ReturnsThe class hash of the contract's originating code.

Fully qualified path: `core::starknet::syscalls::get_class_hash_at_syscall`

<pre><code class="language-rust">pub extern fn get_class_hash_at_syscall(
    contract_address: ContractAddress,
) -&gt; SyscallResult&lt;ClassHash&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

