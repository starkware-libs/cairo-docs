# get_execution_info_v2_syscall

Gets information about the current execution, version 2. This syscall should not be called directly. Instead, use `starknet::info::get_execution_info`.  # ReturnsA box containing the current V2 execution information.

Fully qualified path: `core::starknet::syscalls::get_execution_info_v2_syscall`

<pre><code class="language-rust">pub extern fn get_execution_info_v2_syscall() -&gt; SyscallResult&lt;
    Box&lt;starknet::info::v2::ExecutionInfo&gt;,
&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

