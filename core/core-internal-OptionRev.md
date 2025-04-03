# OptionRev

Same as `Option`, except that the order of the variants is reversed. This is used as the return type of some libfuncs for efficiency reasons.

Fully qualified path: `core::internal::OptionRev`

```rust
#[must_use]
#[derive(Copy, Drop, Debug, PartialEq)]
pub enum OptionRev<T> {
    None,
    Some: T,
}
```

## Variants

### None

Fully qualified path: `core::internal::OptionRev::None`

```rust
None
```


### Some

Fully qualified path: `core::internal::OptionRev::Some`

```rust
Some : T
```


