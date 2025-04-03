# EthAddressSerde

Fully qualified path: `core::starknet::eth_address::EthAddressSerde`

```rust
pub(crate) impl EthAddressSerde of Serde<EthAddress>
```

## Impl functions

### serialize

Fully qualified path: `core::starknet::eth_address::EthAddressSerde::serialize`

```rust
fn serialize(self: @EthAddress, ref output: Array<felt252>)
```


### deserialize

Fully qualified path: `core::starknet::eth_address::EthAddressSerde::deserialize`

```rust
fn deserialize(ref serialized: Span<felt252>) -> Option<EthAddress>
```


