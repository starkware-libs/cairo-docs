# ExecutionInfo

The same as `ExecutionInfo`, but with the `TxInfo` field replaced with `v2::TxInfo`.

Fully qualified path: `core::starknet::info::v2::ExecutionInfo`

```rust
#[derive(Copy, Drop, Debug)]
pub struct ExecutionInfo {
    pub block_info: Box<BlockInfo>,
    pub tx_info: Box<TxInfo>,
    pub caller_address: ContractAddress,
    pub contract_address: ContractAddress,
    pub entry_point_selector: felt252,
}
```

