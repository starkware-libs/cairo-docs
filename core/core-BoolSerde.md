# BoolSerde

Fully qualified path: `core::BoolSerde`

```rust
impl BoolSerde of Serde<bool>
```

## Impl functions

### serialize

Fully qualified path: `core::BoolSerde::serialize`

```rust
fn serialize(self: @bool, ref output: Array<felt252>)
```


### deserialize

Fully qualified path: `core::BoolSerde::deserialize`

```rust
fn deserialize(ref serialized: Span<felt252>) -> Option<bool>
```


