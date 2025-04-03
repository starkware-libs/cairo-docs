# Clone

A common trait for the ability to explicitly duplicate an object.  Differs from `Copy` in that `Copy` is implicit and inexpensive, while `Clone` is always explicit and may or may not be expensive.  Since `Clone` is more general than `Copy`, you can automatically make anything `Copy` be `Clone` as well.  ## Derivable  This trait can be used with `#[derive]` if all fields are `Clone`. The `derive`d implementation of `Clone` calls `clone` on each field.

Fully qualified path: `core::clone::Clone`

```rust
pub trait Clone<T>
```

## Trait functions

### clone

Returns a copy of the value.  # Examples
```cairo
let arr = array![1, 2, 3];
assert!(arr == arr.clone());
```

Fully qualified path: `core::clone::Clone::clone`

```rust
fn clone(self: @T) -> T
```


