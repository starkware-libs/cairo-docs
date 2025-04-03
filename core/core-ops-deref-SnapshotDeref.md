# SnapshotDeref

A helper trait for dereferencing a snapshot of a type. Should not be implemented for copyable types.

Fully qualified path: `core::ops::deref::SnapshotDeref`

```rust
pub trait SnapshotDeref<T>
```

## Trait functions

### snapshot_deref

Returns the dereferenced value.

Fully qualified path: `core::ops::deref::SnapshotDeref::snapshot_deref`

```rust
fn snapshot_deref(self: @T) -> Self::Target
```


## Trait types

### Target

The type of the dereferenced value.

Fully qualified path: `core::ops::deref::SnapshotDeref::Target`

```rust
type Target;
```


