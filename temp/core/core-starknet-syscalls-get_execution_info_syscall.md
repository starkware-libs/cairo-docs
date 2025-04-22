# get_execution_info_syscall

Gets information about the current execution.

Fully qualified path: `core::starknet::syscalls::get_execution_info_syscall`

```rust
pub extern fn get_execution_info_syscall() -> SyscallResult<
    Box<starknet::info::ExecutionInfo>,
> implicits(GasBuiltin, System) nopanic;
```

