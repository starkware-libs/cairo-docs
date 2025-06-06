# into_felt252_based

Implementations for `Debug` and `LowerHex` for types that can be converted into `felt252` using
the `Into` trait.
# Examples

```cairo
impl MyTypeDebug = crate::fmt::into_felt252_based::DebugImpl<MyType>;`
impl MyTypeLowerHex = crate::fmt::into_felt252_based::LowerHexImpl<MyType>;
```

Fully qualified path: [core](./core.md)::[fmt](./core-fmt.md)::[into_felt252_based](./core-fmt-into_felt252_based.md)

