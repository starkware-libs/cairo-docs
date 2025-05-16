# SyscallResultTrait

Trait for handling syscall results.

Fully qualified path: `core::starknet::SyscallResultTrait`

<pre><code class="language-rust">pub trait SyscallResultTrait&lt;T&gt;</code></pre>

## Trait functions

### unwrap_syscall

Unwraps a syscall result, yielding the content of an `Ok`.  # PanicsPanics with the syscall error message if the value is an `Err`.  # Examples
```cairo
let result = starknet::syscalls::get_execution_info_v2_syscall();
let info = result.unwrap_syscall();
```

Fully qualified path: `core::starknet::SyscallResultTrait::unwrap_syscall`

<pre><code class="language-rust">fn unwrap_syscall(self: SyscallResult&lt;T&gt;) -&gt; T</code></pre>


