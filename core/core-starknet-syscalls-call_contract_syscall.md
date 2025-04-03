# call_contract_syscall

Calls a given contract. `address` - The address of the called contract. `entry_point_selector` - A selector for a function within that contract. `calldata` - Call arguments.

Fully qualified path: `core::starknet::syscalls::call_contract_syscall`

```rust
pub extern fn call_contract_syscall(
    address: ContractAddress, entry_point_selector: felt252, calldata: Span<felt252>,
) -> SyscallResult<Span<felt252>> implicits(GasBuiltin, System) nopanic;
```

