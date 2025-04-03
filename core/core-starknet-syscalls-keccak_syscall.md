# keccak_syscall

Computes the keccak of the input. The system call does not add any padding and the input needs to be a multiple of 1088 bits (== 17 u64 word).

Fully qualified path: `core::starknet::syscalls::keccak_syscall`

```rust
pub extern fn keccak_syscall(
    input: Span<u64>,
) -> SyscallResult<u256> implicits(GasBuiltin, System) nopanic;
```

