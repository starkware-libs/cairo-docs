# HashState

State for Poseidon hash.

Fully qualified path: `core::poseidon::HashState`

```rust
#[derive(Copy, Drop, Debug)]
pub struct HashState {
    pub s0: felt252,
    pub s1: felt252,
    pub s2: felt252,
    pub odd: bool,
}
```

