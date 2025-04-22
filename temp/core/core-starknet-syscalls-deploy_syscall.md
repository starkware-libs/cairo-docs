# deploy_syscall

Deploys a new instance of a previously declared class. `class_hash` - The class hash of the contract to be deployed. `contract_address_salt` - The salt, an arbitrary value provided by the sender, used in thecomputation of the contract's address.
`calldata` - Call arguments for the constructor.`deploy_from_zero` - Deploy the contract from the zero address.Returns the address of the deployed contract and the serialized return value of the constructor.

Fully qualified path: `core::starknet::syscalls::deploy_syscall`

```rust
pub extern fn deploy_syscall(
    class_hash: ClassHash,
    contract_address_salt: felt252,
    calldata: Span<felt252>,
    deploy_from_zero: bool,
) -> SyscallResult<(ContractAddress, Span<felt252>)> implicits(GasBuiltin, System) nopanic;
```

