# LegacyHash

Trait for hashing values. Used for backwards compatibility. NOTE: Implement `Hash` instead of this trait if possible.

Fully qualified path: `core::hash::LegacyHash`

```rust
pub trait LegacyHash<T>
```

## Trait functions

### hash

Fully qualified path: `core::hash::LegacyHash::hash`

```rust
fn hash(state: felt252, value: T) -> felt252
```


