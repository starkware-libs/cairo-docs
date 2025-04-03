# circuit_inverse

Given a circuit element, returns a new circuit element representing the circuit that applies the inverse operation on the input circuit.

Fully qualified path: `core::circuit::circuit_inverse`

```rust
pub fn circuit_inverse<Input, +CircuitElementTrait<Input>>(
    input: CircuitElement<Input>,
) -> CircuitElement::<InverseGate<Input>>
```

