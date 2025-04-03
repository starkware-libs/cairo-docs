# PrintTrait

A trait for printing values for debugging purposes. Accessible with prelude editions prior to `2024_07`.  # Examples
```cairo
use core::debug::PrintTrait;

1.print();
(1 == 2).print();

let mut arr = array![];
arr.append('1234567890123456789012345678901');
arr.append('Sca');
arr.append('SomeVeryLongMessage');
arr.print();
```

Fully qualified path: `core::debug::PrintTrait`

```rust
pub(crate) trait PrintTrait<T>
```

## Trait functions

### print

Fully qualified path: `core::debug::PrintTrait::print`

```rust
fn print(self: T)
```


