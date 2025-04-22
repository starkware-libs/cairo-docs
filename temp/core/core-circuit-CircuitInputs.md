# CircuitInputs

Fully qualified path: `core::circuit::CircuitInputs`

```rust
pub trait CircuitInputs<CES>
```

## Trait functions

### new_inputs

calls `init_circuit_data` for the given circuit.

Fully qualified path: `core::circuit::CircuitInputs::new_inputs`

```rust
fn new_inputs<impl CD: CircuitDefinition<CES>, +Drop<CES>>(
    self: CES,
) -> AddInputResult<CD::CircuitType>
```


