# pop_l2_to_l1_message

Pop the earliest unpopped l2 to l1 message for the contract.  # Arguments  `address` - The contract address from which to pop a l2-L1 message.  The returned value is a tuple of the l1 address the message was sent to as a `felt252`, and the message data as a span. May be called multiple times to pop multiple messages. Useful for testing the contract's l2 to l1 message emission.

Fully qualified path: `core::starknet::testing::pop_l2_to_l1_message`

```rust
pub fn pop_l2_to_l1_message(address: ContractAddress) -> Option<(felt252, Span<felt252>)>
```

