# Fn

The version of the call operator that takes a by-snapshot receiver.  Instances of `Fn` can be called multiple times.  `Fn` is implemented automatically by closures that capture only copyable variables.

Fully qualified path: `core::ops::function::Fn`

```rust
pub trait Fn<T, Args>
```

## Trait functions

### call

Performs the call operation.

Fully qualified path: `core::ops::function::Fn::call`

```rust
fn call(self: @T, args: Args) -> Self::Output
```


## Trait types

### Output

The returned type after the call operator is used.

Fully qualified path: `core::ops::function::Fn::Output`

```rust
type Output;
```


