# Deref

A trait for dereferencing a value. This is used in order to directly access members of the dereferenced value.

Fully qualified path: `core::ops::deref::Deref`

```rust
pub trait Deref<T>
```

## Trait functions

### deref

Returns the dereferenced value.

Fully qualified path: `core::ops::deref::Deref::deref`

```rust
fn deref(self: T) -> Self::Target
```


## Trait types

### Target

The type of the dereferenced value.

Fully qualified path: `core::ops::deref::Deref::Target`

```rust
type Target;
```


