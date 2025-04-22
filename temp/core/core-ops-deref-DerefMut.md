# DerefMut

A trait for dereferencing a value. This is used in order to handle the case where the value is a reference.

Fully qualified path: `core::ops::deref::DerefMut`

```rust
pub trait DerefMut<T>
```

## Trait functions

### deref_mut

Returns the dereferenced value.

Fully qualified path: `core::ops::deref::DerefMut::deref_mut`

```rust
fn deref_mut(ref self: T) -> Self::Target
```


## Trait types

### Target

The type of the dereferenced value.

Fully qualified path: `core::ops::deref::DerefMut::Target`

```rust
type Target;
```


