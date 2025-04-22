# get_block_hash_syscall

Gets the block hash of the block with the given number.

Fully qualified path: `core::starknet::syscalls::get_block_hash_syscall`

```rust
pub extern fn get_block_hash_syscall(
    block_number: u64,
) -> SyscallResult<felt252> implicits(GasBuiltin, System) nopanic;
```

