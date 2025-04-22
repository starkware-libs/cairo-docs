# get_execution_info_v2_syscall

Gets information about the current execution, version 2.

Fully qualified path: `core::starknet::syscalls::get_execution_info_v2_syscall`

```rust
pub extern fn get_execution_info_v2_syscall() -> SyscallResult<
    Box<starknet::info::v2::ExecutionInfo>,
> implicits(GasBuiltin, System) nopanic;
```

