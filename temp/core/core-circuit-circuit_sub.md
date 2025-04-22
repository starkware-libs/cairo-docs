# circuit_sub

Given two circuit elements, returns a new circuit element representing the circuit that applies the `submod` operation to the two input circuits.

Fully qualified path: `core::circuit::circuit_sub`

```rust
pub fn circuit_sub<Lhs, Rhs, +CircuitElementTrait<Lhs>, +CircuitElementTrait<Rhs>>(
    lhs: CircuitElement<Lhs>, rhs: CircuitElement<Rhs>,
) -> CircuitElement::<SubModGate<Lhs, Rhs>>
```

