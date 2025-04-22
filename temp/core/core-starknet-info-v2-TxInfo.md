# TxInfo

Fully qualified path: `core::starknet::info::v2::TxInfo`

```rust
#[derive(Copy, Drop, Debug, Serde)]
pub struct TxInfo {
    pub version: felt252,
    pub account_contract_address: ContractAddress,
    pub max_fee: u128,
    pub signature: Span<felt252>,
    pub transaction_hash: felt252,
    pub chain_id: felt252,
    pub nonce: felt252,
    pub resource_bounds: Span<ResourceBounds>,
    pub tip: u128,
    pub paymaster_data: Span<felt252>,
    pub nonce_data_availability_mode: u32,
    pub fee_data_availability_mode: u32,
    pub account_deployment_data: Span<felt252>,
}
```

