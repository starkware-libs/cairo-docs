# emit_event_syscall

Emits an event. `keys` - The keys of the event. `data` - The data of the event.

Fully qualified path: `core::starknet::syscalls::emit_event_syscall`

```rust
pub extern fn emit_event_syscall(
    keys: Span<felt252>, data: Span<felt252>,
) -> SyscallResult<()> implicits(GasBuiltin, System) nopanic;
```

