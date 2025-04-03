# BoolTrait

Fully qualified path: `core::boolean::BoolTrait`

```rust
pub trait BoolTrait<T, +Drop<T>>
```

## Trait functions

### then_some

Returns `Option::Some(t)` if the `bool` is `true`, `Option::None` otherwise.  # Examples
```cairo
assert!(false.then_some(0) == Option::None);
assert!(true.then_some(0) == Option::Some(0));
```

Fully qualified path: `core::boolean::BoolTrait::then_some`

```rust
fn then_some(self: bool, t: T) -> Option<T> nopanic
```


