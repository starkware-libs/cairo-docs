# FnOnce

The version of the call operator that takes a by-value receiver.  Instances of `FnOnce` can be called, but might not be callable multiple times. Because of this, if the only thing known about a type is that it implements `FnOnce`, it can only be called once.  `FnOnce` is implemented automatically by closures that might consume captured variables.
```cairo
```

Fully qualified path: `core::ops::function::FnOnce`

```rust
pub trait FnOnce<T, Args>
```

## Trait functions

### call

Performs the call operation.

Fully qualified path: `core::ops::function::FnOnce::call`

```rust
fn call(self: T, args: Args) -> Self::Output
```


## Trait types

### Output

The returned type after the call operator is used.

Fully qualified path: `core::ops::function::FnOnce::Output`

```rust
type Output;
```


