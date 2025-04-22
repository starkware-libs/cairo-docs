# circuit_add

Given two circuit elements, returns a new circuit element representing the circuit that applies the `addmod` operation to the two input circuits.

Fully qualified path: `core::circuit::circuit_add`

```rust
pub fn circuit_add<Lhs, Rhs, +CircuitElementTrait<Lhs>, +CircuitElementTrait<Rhs>>(
    lhs: CircuitElement<Lhs>, rhs: CircuitElement<Rhs>,
) -> CircuitElement::<AddModGate<Lhs, Rhs>>
```

