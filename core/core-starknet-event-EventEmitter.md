# EventEmitter

Fully qualified path: `core::starknet::event::EventEmitter`

```rust
pub trait EventEmitter<T, TEvent>
```

## Trait functions

### emit

Fully qualified path: `core::starknet::event::EventEmitter::emit`

```rust
fn emit<S, +Into<S, TEvent>>(ref self: T, event: S)
```


