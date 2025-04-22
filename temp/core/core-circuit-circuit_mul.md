# circuit_mul

Given two circuit elements, returns a new circuit element representing the circuit that applies the `mul` operation to the two input circuits.

Fully qualified path: `core::circuit::circuit_mul`

```rust
pub fn circuit_mul<Lhs, Rhs, +CircuitElementTrait<Lhs>, +CircuitElementTrait<Rhs>>(
    lhs: CircuitElement<Lhs>, rhs: CircuitElement<Rhs>,
) -> CircuitElement::<MulModGate<Lhs, Rhs>>
```

