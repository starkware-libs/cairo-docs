# storage_read_syscall

Gets the value of a key in the storage of the calling contract.  # Arguments`address_domain` - The domain of the address. Only `address_domain` 0 is currently supported, in the future it will enable access to address spaces with different data availability guarantees. * `address` - The address of the storage key to read.

Fully qualified path: `core::starknet::syscalls::storage_read_syscall`

<pre><code class="language-rust">pub extern fn storage_read_syscall(
    address_domain: u32, address: StorageAddress,
) -&gt; SyscallResult&lt;felt252&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

