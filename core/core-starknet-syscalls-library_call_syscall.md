# library_call_syscall

Calls the requested function in any previously declared class. `class_hash` - The hash of the class you want to use. `function_selector` - A selector for a function within that class. `calldata` - Call arguments.

Fully qualified path: `core::starknet::syscalls::library_call_syscall`

```rust
pub extern fn library_call_syscall(
    class_hash: ClassHash, function_selector: felt252, calldata: Span<felt252>,
) -> SyscallResult<Span<felt252>> implicits(GasBuiltin, System) nopanic;
```

