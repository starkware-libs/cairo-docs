# circuit

Efficient modular arithmetic computations using arithmetic circuits.This module provides a type-safe way to perform modular arithmetic operations using arithmetic circuits. It is particularly useful for implementing cryptographic algorithms and other computations that require efficient modular arithmetic with large numbers.  # Core FeaturesModular arithmetic operations (add, subtract, multiply, inverse) - Support for numbers up to 384 bits - Type-safe circuit construction - Efficient evaluation of complex expressions  # Examples  ## Basic ArithmeticHere's an example showing basic modular arithmetic operations:
```cairo
use core::circuit::{
   CircuitElement, EvalCircuitTrait, CircuitOutputsTrait, CircuitInput, CircuitModulus,
   AddInputResultTrait, CircuitInputs, circuit_add, circuit_mul,
};

// Compute (a + b) * c mod p
let a = CircuitElement::<CircuitInput<0>> {};
let b = CircuitElement::<CircuitInput<1>> {};
let c = CircuitElement::<CircuitInput<2>> {};

let sum = circuit_add(a, b);
let result = circuit_mul(sum, c);

// Evaluate with inputs [3, 6, 2] modulo 7
let modulus = TryInto::<_, CircuitModulus>::try_into([7, 0, 0, 0]).unwrap();
let outputs = (result,)
    .new_inputs()
    .next([3, 0, 0, 0])
    .next([6, 0, 0, 0])
    .next([2, 0, 0, 0])
    .done()
    .eval(modulus)
    .unwrap();

// Result: (3 + 6) * 2 mod 7 = 4
assert!(outputs.get_output(result) == 4.into());
```
  # How It WorksThe module uses a type-based approach to construct and evaluate arithmetic circuits:Circuit elements are created using `CircuitElement<T>` where T defines their role (input or gate) 2. Basic operations combine elements into more complex expressions (chaining gates to create a circuit) 3. The final circuit is evaluated with specific input values and a modulusOperations are performed using a multi-limb representation for large numbers, with each number represented as four 96-bit limbs allowing for values up to 384 bits.  # Performance ConsiderationsCircuit evaluation is optimized for large modular arithmetic operations - The multi-limb representation allows efficient handling of large numbers - Circuit construction has zero runtime overhead due to type-based approach  # ErrorsCircuit evaluation can fail in certain cases: - When computing multiplicative inverses of non-invertible elements - When the modulus is 0 or 1 In that case the evaluation will return an Error.

Fully qualified path: `core::circuit`

## Free functions

- [circuit_add](./core-circuit-circuit_add.md)

- [circuit_sub](./core-circuit-circuit_sub.md)

- [circuit_inverse](./core-circuit-circuit_inverse.md)

- [circuit_mul](./core-circuit-circuit_mul.md)

## Structs

- [u384](./core-circuit-u384.md)

- [CircuitElement](./core-circuit-CircuitElement.md)

## Enums

- [AddInputResult](./core-circuit-AddInputResult.md)

## Type aliases

- [u96](./core-circuit-u96.md)

- [ConstZero](./core-circuit-ConstZero.md)

- [ConstOne](./core-circuit-ConstOne.md)

## Traits

- [CircuitElementTrait](./core-circuit-CircuitElementTrait.md)

- [CircuitDefinition](./core-circuit-CircuitDefinition.md)

- [CircuitOutputsTrait](./core-circuit-CircuitOutputsTrait.md)

- [CircuitInputs](./core-circuit-CircuitInputs.md)

- [AddInputResultTrait](./core-circuit-AddInputResultTrait.md)

- [EvalCircuitTrait](./core-circuit-EvalCircuitTrait.md)

## Impls

- [CircuitElementDrop](./core-circuit-CircuitElementDrop.md)

- [CircuitElementCopy](./core-circuit-CircuitElementCopy.md)

- [DestructFailureGuarantee](./core-circuit-DestructFailureGuarantee.md)

## Extern types

- [RangeCheck96](./core-circuit-RangeCheck96.md)

- [AddMod](./core-circuit-AddMod.md)

- [MulMod](./core-circuit-MulMod.md)

- [CircuitModulus](./core-circuit-CircuitModulus.md)

- [Circuit](./core-circuit-Circuit.md)

- [CircuitInput](./core-circuit-CircuitInput.md)

