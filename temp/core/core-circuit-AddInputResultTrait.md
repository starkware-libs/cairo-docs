# AddInputResultTrait

Fully qualified path: `core::circuit::AddInputResultTrait`

```rust
pub trait AddInputResultTrait<C>
```

## Trait functions

### next

Adds an input to the accumulator.

Fully qualified path: `core::circuit::AddInputResultTrait::next`

```rust
fn next<Value, +IntoCircuitInputValue<Value>, +Drop<Value>>(
    self: AddInputResult<C>, value: Value,
) -> AddInputResult<C>
```


### done

Fully qualified path: `core::circuit::AddInputResultTrait::done`

```rust
fn done(self: AddInputResult<C>) -> CircuitData<C>
```


