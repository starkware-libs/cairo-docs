# TupleSplit

A trait for splitting a tuple into head element and a tail tuple, as well as reconstructing from them.

Fully qualified path: `core::metaprogramming::TupleSplit`

```rust
pub(crate) trait TupleSplit<T>
```

## Trait functions

### split_head

Splits the tuple into the head and the rest.

Fully qualified path: `core::metaprogramming::TupleSplit::split_head`

```rust
fn split_head(self: T) -> (Self::Head, Self::Rest) nopanic
```


### reconstruct

Reconstructs the tuple from the head and the rest.

Fully qualified path: `core::metaprogramming::TupleSplit::reconstruct`

```rust
fn reconstruct(head: Self::Head, rest: Self::Rest) -> T nopanic
```


## Trait types

### Head

The type of the first element of the tuple.

Fully qualified path: `core::metaprogramming::TupleSplit::Head`

```rust
type Head;
```


### Rest

The type of the rest of the tuple.

Fully qualified path: `core::metaprogramming::TupleSplit::Rest`

```rust
type Rest;
```


