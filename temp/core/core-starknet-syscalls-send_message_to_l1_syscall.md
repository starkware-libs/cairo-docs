# send_message_to_l1_syscall

Sends a message to L1. `to_address` - The recipient's L1 address. `payload` - The content of the message.

Fully qualified path: `core::starknet::syscalls::send_message_to_l1_syscall`

```rust
pub extern fn send_message_to_l1_syscall(
    to_address: felt252, payload: Span<felt252>,
) -> SyscallResult<()> implicits(GasBuiltin, System) nopanic;
```

