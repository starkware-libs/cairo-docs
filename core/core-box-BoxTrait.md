# BoxTrait

Fully qualified path: `core::box::BoxTrait`

```rust
pub trait BoxTrait<T>
```

## Trait functions

### new

Creates a new `Box` with the given value.  Allocates space in the boxed segment for the provided value and returns a `Box<T>` that points to it. # Examples
```cairo
let x = 42;
let boxed_x = BoxTrait::new(x);
```

Fully qualified path: `core::box::BoxTrait::new`

```rust
fn new(value: T) -> Box<T> nopanic
```


### unbox

Unboxes the given `Box` and returns the wrapped value.  # Examples
```cairo
let boxed = BoxTrait::new(42);
assert!(boxed.unbox() == 42);
```

Fully qualified path: `core::box::BoxTrait::unbox`

```rust
fn unbox(self: Box<T>) -> T nopanic
```


### as_snapshot

Converts the given snapshot of a `Box` into a `Box` of a snapshot. Useful for structures that aren't copyable.  # Examples
```cairo
let snap_boxed_arr = @BoxTraits::new(array![1, 2, 3]);
let boxed_snap_arr = snap_boxed_arr.as_snapshot();
let snap_arr = boxed_snap_arr.unbox();
```

Fully qualified path: `core::box::BoxTrait::as_snapshot`

```rust
fn as_snapshot(self: @Box<T>) -> Box<@T> nopanic
```


