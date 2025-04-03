# OptionTrait

Fully qualified path: `core::option::OptionTrait`

```rust
pub trait OptionTrait<T>
```

## Trait functions

### expect

If `val` is `Option::Some(x)`, returns `x`. Otherwise, panics with `err`.

Fully qualified path: `core::option::OptionTrait::expect`

```rust
fn expect(self: Option<T>, err: felt252) -> T
```


### unwrap

If `val` is `Option::Some(x)`, returns `x`. Otherwise, panics.

Fully qualified path: `core::option::OptionTrait::unwrap`

```rust
fn unwrap(self: Option<T>) -> T
```


### ok_or

Transforms the `Option<T>` into a `Result<T, E>`, mapping `Option::Some(v)` to `Result::Ok(v)` and `Option::None` to `Result::Err(err)`.

Fully qualified path: `core::option::OptionTrait::ok_or`

```rust
fn ok_or<E, +Destruct<E>>(self: Option<T>, err: E) -> Result<T, E>
```


### is_some

Returns `true` if the `Option` is `Option::Some`.

Fully qualified path: `core::option::OptionTrait::is_some`

```rust
fn is_some(self: @Option<T>) -> bool
```


### is_none

Returns `true` if the `Option` is `Option::None`.

Fully qualified path: `core::option::OptionTrait::is_none`

```rust
fn is_none(self: @Option<T>) -> bool
```


### unwrap_or

If `self` is `Option::Some(x)`, returns `x`. Otherwise, returns the provided default.

Fully qualified path: `core::option::OptionTrait::unwrap_or`

```rust
fn unwrap_or<+Destruct<T>>(self: Option<T>, default: T) -> T
```


### unwrap_or_default

If `self` is `Option::Some(x)`, returns `x`. Otherwise, returns `Default::<T>::default()`.

Fully qualified path: `core::option::OptionTrait::unwrap_or_default`

```rust
fn unwrap_or_default<+Default<T>>(self: Option<T>) -> T
```


