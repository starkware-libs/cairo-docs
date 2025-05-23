# get_execution_info_syscall

Gets information about the currently executing block and the transactions in the block. For a complete description of this information, see [`Execution information`](`Execution information`).When an account’s `__validate__`, `__validate_deploy__`, or `__validate_declare__` function calls `get_execution_info`, the return values for `block_timestamp` and `block_number` are modified as follows: * `block_timestamp` returns the hour, rounded down to the nearest hour. * `block_number` returns the block number, rounded down to the nearest multiple of 100.  # ReturnsA struct that contains information about the currently executing function, transaction, and block.

Fully qualified path: `core::starknet::syscalls::get_execution_info_syscall`

<pre><code class="language-rust">pub extern fn get_execution_info_syscall() -&gt; SyscallResult&lt;
    Box&lt;starknet::info::ExecutionInfo&gt;,
&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

