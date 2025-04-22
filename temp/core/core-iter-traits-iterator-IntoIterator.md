# IntoIterator

Turn a collection of values into an iterator.

Fully qualified path: `core::iter::traits::iterator::IntoIterator`

```rust
pub trait IntoIterator<T>
```

## Trait functions

### into_iter

Creates an iterator from a collection.

Fully qualified path: `core::iter::traits::iterator::IntoIterator::into_iter`

```rust
fn into_iter(self: T) -> Self::IntoIter
```


## Trait types

### IntoIter

The iterator type that will be created.

Fully qualified path: `core::iter::traits::iterator::IntoIterator::IntoIter`

```rust
type IntoIter;
```


