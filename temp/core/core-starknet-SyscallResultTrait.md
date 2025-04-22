# SyscallResultTrait

Fully qualified path: `core::starknet::SyscallResultTrait`

```rust
pub trait SyscallResultTrait<T>
```

## Trait functions

### unwrap_syscall

If `val` is `Result::Ok(x)`, returns `x`. Otherwise, panics with the revert reason.

Fully qualified path: `core::starknet::SyscallResultTrait::unwrap_syscall`

```rust
fn unwrap_syscall(self: SyscallResult<T>) -> T
```


