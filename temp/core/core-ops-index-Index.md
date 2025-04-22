# Index

Trait for accessing an item contained in type `C` with an index of type `I`.

Fully qualified path: `core::ops::index::Index`

```rust
pub trait Index<C, I>
```

## Trait functions

### index

Returns the item at the given index.

Fully qualified path: `core::ops::index::Index::index`

```rust
fn index(ref self: C, index: I) -> Self::Target
```


## Trait types

### Target

The type of the item.

Fully qualified path: `core::ops::index::Index::Target`

```rust
type Target;
```


