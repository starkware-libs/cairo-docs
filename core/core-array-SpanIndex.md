# SpanIndex

Fully qualified path: `core::array::SpanIndex`

```rust
pub impl SpanIndex<T> of IndexView<Span<T>, usize, @T>
```

## Impl functions

### index

Returns a snapshot of the element at the given index.  # Examples
```cairo
let span: @Span<u8> = @array![1, 2, 3].span();
let element: @u8 = span[0];
assert!(element == @1);
```

Fully qualified path: `core::array::SpanIndex::index`

```rust
fn index(self: @Span<T>, index: usize) -> @T
```


