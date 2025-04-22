# sha256_process_block_syscall

Computes the next sha256 state of the input with the given state. The system call does not add any padding and the input needs to be a multiple of 512 bits (== 16 u32 word).

Fully qualified path: `core::starknet::syscalls::sha256_process_block_syscall`

```rust
pub extern fn sha256_process_block_syscall(
    state: core::sha256::Sha256StateHandle, input: Box<[u32; 16]>,
) -> SyscallResult<core::sha256::Sha256StateHandle> implicits(GasBuiltin, System) nopanic;
```

