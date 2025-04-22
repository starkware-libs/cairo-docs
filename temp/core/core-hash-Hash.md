# Hash

A trait for values that can be hashed.

Fully qualified path: `core::hash::Hash`

```rust
pub trait Hash<T, S, +HashStateTrait<S>>
```

## Trait functions

### update_state

Updates the hash state with the given value.

Fully qualified path: `core::hash::Hash::update_state`

```rust
fn update_state(state: S, value: T) -> S
```


