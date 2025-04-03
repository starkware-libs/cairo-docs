# AbsAndSign

Internal trait for easier finding of absolute values.

Fully qualified path: `core::integer::AbsAndSign`

```rust
pub(crate) trait AbsAndSign<Signed, Unsigned>
```

## Trait functions

### abs_and_sign

Returns the absolute value of the `Signed` value as `Unsigned` and the original sign. Returns `true` for sign if the number was negative and `false` otherwise.

Fully qualified path: `core::integer::AbsAndSign::abs_and_sign`

```rust
fn abs_and_sign(self: Signed) -> (Unsigned, bool)
```


