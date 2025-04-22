# Bytes31Trait

Fully qualified path: `core::bytes_31::Bytes31Trait`

```rust
pub trait Bytes31Trait
```

## Trait functions

### at

Returns the byte at the given index (LSB's index is 0).  Assumes that `index < BYTES_IN_BYTES31`. If the assumption is not met, the behavior is undefined.  # Examples
```cairo
let bytes: bytes31 = 1_u8.into();
assert!(bytes.at(0) == 1);
```

Fully qualified path: `core::bytes_31::Bytes31Trait::at`

```rust
fn at(self: @bytes31, index: usize) -> u8
```


