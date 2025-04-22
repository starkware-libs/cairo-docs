# BlockInfo

Information about the current block.

Fully qualified path: `core::starknet::info::BlockInfo`

```rust
#[derive(Copy, Drop, Debug, Serde)]
pub struct BlockInfo {
    pub block_number: u64,
    pub block_timestamp: u64,
    pub sequencer_address: ContractAddress,
}
```

