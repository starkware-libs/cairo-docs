# PedersenTrait

Fully qualified path: `core::pedersen::PedersenTrait`

```rust
pub trait PedersenTrait
```

## Trait functions

### new

Creates a new Pedersen hash state with the given base value.  # Examples
```cairo
use core::pedersen::PedersenTrait;

let mut state = PedersenTrait::new(0);
assert!(state.state == 0);
```

Fully qualified path: `core::pedersen::PedersenTrait::new`

```rust
fn new(base: felt252) -> HashState
```


