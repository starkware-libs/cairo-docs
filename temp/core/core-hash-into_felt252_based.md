# into_felt252_based

Impl for `Hash` for types that can be converted into `felt252` using the `Into` trait. Usage example:
```ignore
impl MyTypeHash<S, +HashStateTrait<S>, +Drop<S>> =
    core::hash::into_felt252_based::HashImpl<MyType, S>;`
```

Fully qualified path: `core::hash::into_felt252_based`

