# Span

A span is a view into a continuous collection of the same type - such as `Array`. It is a structure with a single field that holds a snapshot of an array. `Span` implements the `Copy` and the `Drop` traits.

Fully qualified path: `core::array::Span`

```rust
pub struct Span<T> {
    pub(crate) snapshot: @Array<T>,
}
```

