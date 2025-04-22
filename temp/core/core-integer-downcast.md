# downcast

Fully qualified path: `core::integer::downcast`

```rust
pub(crate) extern fn downcast<FromType, ToType>(
    x: FromType,
) -> Option<ToType> implicits(RangeCheck) nopanic;
```

