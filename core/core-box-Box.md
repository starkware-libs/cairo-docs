# Box

A `Box` is a type that points to a wrapped value. It allows for cheap moving around of the value, as its size is small, and may wrap a large size.

Fully qualified path: `core::box::Box`

```rust
#[derive(Copy, Drop)]
pub extern type Box<T>
```

