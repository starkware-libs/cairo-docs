# get_class_hash_at_syscall

Gets the class hash of the contract at the given address. `contract_address` - The address of the deployed contract.  Returns the class hash of the contract's originating code.

Fully qualified path: `core::starknet::syscalls::get_class_hash_at_syscall`

```rust
pub extern fn get_class_hash_at_syscall(
    contract_address: ContractAddress,
) -> SyscallResult<ClassHash> implicits(GasBuiltin, System) nopanic;
```

