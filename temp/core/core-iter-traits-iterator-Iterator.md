# Iterator

An iterator over a collection of values.

Fully qualified path: `core::iter::traits::iterator::Iterator`

```rust
pub trait Iterator<T>
```

## Trait functions

### next

Advance the iterator and return the next value.

Fully qualified path: `core::iter::traits::iterator::Iterator::next`

```rust
fn next(ref self: T) -> Option<Self::Item>
```


## Trait types

### Item

The type of the elements being iterated over.

Fully qualified path: `core::iter::traits::iterator::Iterator::Item`

```rust
type Item;
```


