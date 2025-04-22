# IndexView

The following two traits are for implementing the [] operator. Only one should be implemented for each type. Both are not consuming of self, the first gets a snapshot of the object and the second gets ref. Trait for a view of an item contained in type `C` with an index of type `I`.

Fully qualified path: `core::ops::index::IndexView`

```rust
pub trait IndexView<C, I>
```

## Trait functions

### index

Returns the item at the given index.

Fully qualified path: `core::ops::index::IndexView::index`

```rust
fn index(self: @C, index: I) -> Self::Target
```


## Trait types

### Target

The type of the item.

Fully qualified path: `core::ops::index::IndexView::Target`

```rust
type Target;
```


