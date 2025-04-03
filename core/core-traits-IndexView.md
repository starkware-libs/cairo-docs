# IndexView

The following two traits are for implementing the [] operator. Only one should be implemented for each type. Both are not consuming of self, the first gets a snapshot of the object and the second gets ref.

Fully qualified path: `core::traits::IndexView`

```rust
pub trait IndexView<C, I, V>
```

## Trait functions

### index

Fully qualified path: `core::traits::IndexView::index`

```rust
fn index(self: @C, index: I) -> V
```


