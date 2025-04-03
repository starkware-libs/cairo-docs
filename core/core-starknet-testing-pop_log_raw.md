# pop_log_raw

Pop the earliest unpopped logged event for the contract.  # Arguments  `address` - The contract address from which to pop an event.  The value is returned as a tuple of two spans, the first for the keys and the second for the data. May be called multiple times to pop multiple events. If called until `None` is returned, all events have been popped.

Fully qualified path: `core::starknet::testing::pop_log_raw`

```rust
pub fn pop_log_raw(address: ContractAddress) -> Option<(Span<felt252>, Span<felt252>)>
```

