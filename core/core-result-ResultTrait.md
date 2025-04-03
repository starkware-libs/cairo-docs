# ResultTrait

Fully qualified path: `core::result::ResultTrait`

```rust
pub trait ResultTrait<T, E>
```

## Trait functions

### expect

If `val` is `Result::Ok(x)`, returns `x`. Otherwise, panics with `err`.

Fully qualified path: `core::result::ResultTrait::expect`

```rust
fn expect<+PanicDestruct<E>>(self: Result<T, E>, err: felt252) -> T
```


### unwrap

If `val` is `Result::Ok(x)`, returns `x`. Otherwise, panics.

Fully qualified path: `core::result::ResultTrait::unwrap`

```rust
fn unwrap<+Destruct<E>>(self: Result<T, E>) -> T
```


### unwrap_or

If `val` is `Result::Ok(x)`, returns `x`. Otherwise, returns `default`.

Fully qualified path: `core::result::ResultTrait::unwrap_or`

```rust
fn unwrap_or<+Destruct<T>, +Destruct<E>>(self: Result<T, E>, default: T) -> T
```


### unwrap_or_default

If `val` is `Result::Ok(x)`, returns `x`. Otherwise returns `Default::<T>::default()`.

Fully qualified path: `core::result::ResultTrait::unwrap_or_default`

```rust
fn unwrap_or_default<+Destruct<E>, +Default<T>>(self: Result<T, E>) -> T
```


### expect_err

If `val` is `Result::Err(x)`, returns `x`. Otherwise, panics with `err`.

Fully qualified path: `core::result::ResultTrait::expect_err`

```rust
fn expect_err<+PanicDestruct<T>>(self: Result<T, E>, err: felt252) -> E
```


### unwrap_err

If `val` is `Result::Err(x)`, returns `x`. Otherwise, panics.

Fully qualified path: `core::result::ResultTrait::unwrap_err`

```rust
fn unwrap_err<+PanicDestruct<T>>(self: Result<T, E>) -> E
```


### is_ok

Returns `true` if the `Result` is `Result::Ok`.

Fully qualified path: `core::result::ResultTrait::is_ok`

```rust
fn is_ok(self: @Result<T, E>) -> bool
```


### is_err

Returns `true` if the `Result` is `Result::Err`.

Fully qualified path: `core::result::ResultTrait::is_err`

```rust
fn is_err(self: @Result<T, E>) -> bool
```


### into_is_err

Returns `true` if the `Result` is `Result::Ok`, and consumes the value.

Fully qualified path: `core::result::ResultTrait::into_is_err`

```rust
fn into_is_err<+Destruct<T>, +Destruct<E>>(self: Result<T, E>) -> bool
```


### into_is_ok

Returns `true` if the `Result` is `Result::Err`, and consumes the value.

Fully qualified path: `core::result::ResultTrait::into_is_ok`

```rust
fn into_is_ok<+Destruct<T>, +Destruct<E>>(self: Result<T, E>) -> bool
```


### ok

Converts from `Result<T, E>` to `Option<T>`.  Converts `self` into an `Option<T>`, consuming `self`, and discarding the error, if any.  # Examples
```cairo
let x: Result<u32, ByteArray> = Result::Ok(2);
assert_eq!(x.ok(), Option::Some(2));

let x: Result<u32, ByteArray> = Result::Err("Nothing here");
assert!(x.ok().is_none());
```

Fully qualified path: `core::result::ResultTrait::ok`

```rust
fn ok<+Destruct<T>, +Destruct<E>>(self: Result<T, E>) -> Option<T>
```


### err

Converts from `Result<T, E>` to `Option<E>`.  Converts `self` into an `Option<E>`, consuming `self`, and discarding the success value, if any.  # Examples
```cairo
let x: Result<u32, ByteArray> = Result::Err("Nothing here");
assert_eq!(x.err(), Option::Some("Nothing here"));

let x: Result<u32, ByteArray> = Result::Ok(2);
assert!(x.err().is_none());
```

Fully qualified path: `core::result::ResultTrait::err`

```rust
fn err<+Destruct<T>, +Destruct<E>>(self: Result<T, E>) -> Option<E>
```


