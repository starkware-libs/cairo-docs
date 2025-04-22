# PoseidonImpl

A trait for creating a new Poseidon hash state.

Fully qualified path: `core::poseidon::PoseidonImpl`

```rust
pub impl PoseidonImpl of PoseidonTrait
```

## Impl functions

### new

Creates an initial state with all fields set to 0.  # Examples
```cairo
use core::poseidon::PoseidonTrait;

let mut state = PoseidonTrait::new();
```

Fully qualified path: `core::poseidon::PoseidonImpl::new`

```rust
fn new() -> HashState
```


