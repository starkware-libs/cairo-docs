# TupleExtendFront

A trait for extending a tuple from the front.

Fully qualified path: `core::metaprogramming::TupleExtendFront`

```rust
pub(crate) trait TupleExtendFront<T, E>
```

## Trait functions

### extend_front

Creates a new tuple from the `value` tuple with `element` in front of it.

Fully qualified path: `core::metaprogramming::TupleExtendFront::extend_front`

```rust
fn extend_front(value: T, element: E) -> Self::Result nopanic
```


## Trait types

### Result

The type of the resulting tuple.

Fully qualified path: `core::metaprogramming::TupleExtendFront::Result`

```rust
type Result;
```


