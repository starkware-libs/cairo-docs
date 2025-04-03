# Call

A struct representing a call to a contract.

Fully qualified path: `core::starknet::account::Call`

```rust
#[derive(Drop, Copy, Serde, Debug)]
pub struct Call {
    pub to: ContractAddress,
    pub selector: felt252,
    pub calldata: Span<felt252>,
}
```

