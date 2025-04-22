# replace_class_syscall

Replaces the class hash of the current contract. `class_hash` - The class hash that should replace the current one.

Fully qualified path: `core::starknet::syscalls::replace_class_syscall`

```rust
pub extern fn replace_class_syscall(
    class_hash: ClassHash,
) -> SyscallResult<()> implicits(GasBuiltin, System) nopanic;
```

