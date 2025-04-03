# FromNullableResult

Represents the result of matching a `Nullable` value.  Used to safely handle both null and non-null cases when using `match_nullable` on a `Nullable`.

Fully qualified path: `core::nullable::FromNullableResult`

```rust
pub enum FromNullableResult<T> {
    Null,
    NotNull: Box<T>,
}
```

## Variants

### Null

Represents a null value

Fully qualified path: `core::nullable::FromNullableResult::Null`

```rust
Null
```


### NotNull

The boxed value when not null

Fully qualified path: `core::nullable::FromNullableResult::NotNull`

```rust
NotNull : Box < T >
```


