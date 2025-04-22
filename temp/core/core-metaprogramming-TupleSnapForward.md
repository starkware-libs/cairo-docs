# TupleSnapForward

A trait for forwarding a wrapping snapshot from a tuple style struct into a tuple style struct of the snapshots.

Fully qualified path: `core::metaprogramming::TupleSnapForward`

```rust
pub(crate) trait TupleSnapForward<T>
```

## Trait functions

### snap_forward

Fully qualified path: `core::metaprogramming::TupleSnapForward::snap_forward`

```rust
fn snap_forward(self: @T) -> Self::SnapForward nopanic
```


## Trait types

### SnapForward

Fully qualified path: `core::metaprogramming::TupleSnapForward::SnapForward`

```rust
type SnapForward;
```


