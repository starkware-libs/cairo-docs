# IsZeroResult

Represents the result of checking whether a value is zero.

Fully qualified path: `core::zeroable::IsZeroResult`

```rust
pub(crate) enum IsZeroResult<T> {
    Zero,
    NonZero: NonZero<T>,
}
```

## Variants

### Zero

Indicates that the value is zero.

Fully qualified path: `core::zeroable::IsZeroResult::Zero`

```rust
Zero
```


### NonZero

Indicates that the value is non-zero, wrapping it in a `NonZero<T>`.

Fully qualified path: `core::zeroable::IsZeroResult::NonZero`

```rust
NonZero : NonZero < T >
```


