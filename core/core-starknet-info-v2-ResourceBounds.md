# ResourceBounds

Fully qualified path: `core::starknet::info::v2::ResourceBounds`

```rust
#[derive(Copy, Drop, Debug, Serde)]
pub struct ResourceBounds {
    pub resource: felt252,
    pub max_amount: u64,
    pub max_price_per_unit: u128,
}
```

