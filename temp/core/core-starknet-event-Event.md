# Event

Fully qualified path: `core::starknet::event::Event`

```rust
pub trait Event<T>
```

## Trait functions

### append_keys_and_data

Fully qualified path: `core::starknet::event::Event::append_keys_and_data`

```rust
fn append_keys_and_data(self: @T, ref keys: Array<felt252>, ref data: Array<felt252>)
```


### deserialize

Fully qualified path: `core::starknet::event::Event::deserialize`

```rust
fn deserialize(ref keys: Span<felt252>, ref data: Span<felt252>) -> Option<T>
```


