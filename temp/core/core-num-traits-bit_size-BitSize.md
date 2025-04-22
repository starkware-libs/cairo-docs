# BitSize

A trait used to retrieve the size of a type in bits.

Fully qualified path: `core::num::traits::bit_size::BitSize`

```rust
pub trait BitSize<T>
```

## Trait functions

### bits

Returns the bit size of `T` as a `usize`.  # Examples
```cairo
use core::num::traits::BitSize;

let bits = BitSize::<u8>::bits();
assert(bits == 8);
```

Fully qualified path: `core::num::traits::bit_size::BitSize::bits`

```rust
fn bits() -> usize
```


