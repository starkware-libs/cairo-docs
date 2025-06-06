# circuit

Efficient modular arithmetic computations using arithmetic circuits.
This module provides a type-safe way to perform modular arithmetic operations using
arithmetic circuits. It is particularly useful for implementing cryptographic algorithms
and other computations that require efficient modular arithmetic with large numbers.
# Core Features

- Modular arithmetic operations (add, subtract, multiply, inverse)
- Support for numbers up to 384 bits
- Type-safe circuit construction
- Efficient evaluation of complex expressions
# Examples
## Basic Arithmetic

Here's an example showing basic modular arithmetic operations:
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
# How It Works

The module uses a type-based approach to construct and evaluate arithmetic circuits:
1. Circuit elements are created using `CircuitElement<T>` where T defines their role (input or
gate)
2. Basic operations combine elements into more complex expressions (chaining gates to create a
circuit)
3. The final circuit is evaluated with specific input values and a modulus

Operations are performed using a multi-limb representation for large numbers,
with each number represented as four 96-bit limbs allowing for values up to 384 bits.
# Performance Considerations

- Circuit evaluation is optimized for large modular arithmetic operations
- The multi-limb representation allows efficient handling of large numbers
- Circuit construction has zero runtime overhead due to type-based approach
# Errors

Circuit evaluation can fail in certain cases:
- When computing multiplicative inverses of non-invertible elements
- When the modulus is 0 or 1
In that case the evaluation will return an Error.

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)


[Free functions](./core-circuit-free_functions.md)
 ---
| | |
|:---|:---|
| [circuit_add](./core-circuit-circuit_add.md) | Creates a new circuit element representing addition modulo p of two input circuits. This function combines two circuit elements using modular addition, creating a new circuit[...](./core-circuit-circuit_add.md) |
| [circuit_sub](./core-circuit-circuit_sub.md) | Creates a new circuit element representing subtraction modulo p of two input circuits. This function combines two circuit elements using modular subtraction, creating a new circuit[...](./core-circuit-circuit_sub.md) |
| [circuit_inverse](./core-circuit-circuit_inverse.md) | Creates a new circuit element representing the multiplicative inverse modulo p of an input circuit. This function creates a new circuit element representing the multiplicative inverse of the input[...](./core-circuit-circuit_inverse.md) |
| [circuit_mul](./core-circuit-circuit_mul.md) | Creates a new circuit element representing multiplication modulo p of two input circuits. This function combines two circuit elements using modular multiplication, creating a new circuit[...](./core-circuit-circuit_mul.md) |

[Structs](./core-circuit-structs.md)
 ---
| | |
|:---|:---|
| [u384](./core-circuit-u384.md) | A 384-bit unsigned integer, used for circuit values.[...](./core-circuit-u384.md) |
| [CircuitElement](./core-circuit-CircuitElement.md) | A wrapper for circuit elements, used to construct circuits. This type provides a generic wrapper around different circuit components (inputs, gates)[...](./core-circuit-CircuitElement.md) |

[Enums](./core-circuit-enums.md)
 ---
| | |
|:---|:---|
| [AddInputResult](./core-circuit-AddInputResult.md) | The result of filling an input in the circuit instance's data. This enum represents the state of input filling process, indicating whether all inputs have been provided or more are needed.[...](./core-circuit-AddInputResult.md) |

[Type aliases](./core-circuit-type_aliases.md)
 ---
| | |
|:---|:---|
| [u96](./core-circuit-u96.md) | A 96-bit unsigned integer type used as the basic building block for multi-limb arithmetic.[...](./core-circuit-u96.md) |
| [ConstZero](./core-circuit-ConstZero.md) | Expose the const required by the libfunc to allow the compiler const reusage.[...](./core-circuit-ConstZero.md) |
| [ConstOne](./core-circuit-ConstOne.md) | [...](./core-circuit-ConstOne.md) |

[Traits](./core-circuit-traits.md)
 ---
| | |
|:---|:---|
| [CircuitElementTrait](./core-circuit-CircuitElementTrait.md) | A marker trait for keeping track of which types are valid circuit elements. This trait is implemented for all valid circuit components including inputs and gates.[...](./core-circuit-CircuitElementTrait.md) |
| [CircuitDefinition](./core-circuit-CircuitDefinition.md) | A trait for defining a circuit's structure and behavior. This trait is used to define the structure of a circuit, including its inputs,[...](./core-circuit-CircuitDefinition.md) |
| [CircuitOutputsTrait](./core-circuit-CircuitOutputsTrait.md) | A trait for retrieving output values from a circuit evaluation. This trait provides methods to access the output values of a circuit after successful evaluation.[...](./core-circuit-CircuitOutputsTrait.md) |
| [CircuitInputs](./core-circuit-CircuitInputs.md) | [...](./core-circuit-CircuitInputs.md) |
| [AddInputResultTrait](./core-circuit-AddInputResultTrait.md) | [...](./core-circuit-AddInputResultTrait.md) |
| [EvalCircuitTrait](./core-circuit-EvalCircuitTrait.md) | [...](./core-circuit-EvalCircuitTrait.md) |

[Impls](./core-circuit-impls.md)
 ---
| | |
|:---|:---|
| [CircuitElementDrop](./core-circuit-CircuitElementDrop.md) | [...](./core-circuit-CircuitElementDrop.md) |
| [CircuitElementCopy](./core-circuit-CircuitElementCopy.md) | [...](./core-circuit-CircuitElementCopy.md) |
| [DestructFailureGuarantee](./core-circuit-DestructFailureGuarantee.md) | [...](./core-circuit-DestructFailureGuarantee.md) |

[Extern types](./core-circuit-extern_types.md)
 ---
| | |
|:---|:---|
| [RangeCheck96](./core-circuit-RangeCheck96.md) | Range check builtin for 96-bit operations.[...](./core-circuit-RangeCheck96.md) |
| [AddMod](./core-circuit-AddMod.md) | Builtin for modular addition operations.[...](./core-circuit-AddMod.md) |
| [MulMod](./core-circuit-MulMod.md) | Builtin for modular multiplication operations.[...](./core-circuit-MulMod.md) |
| [CircuitModulus](./core-circuit-CircuitModulus.md) | A type that can be used as a circuit modulus (a u384 that is not zero or one). The modulus defines the finite field over which the circuit operates. It must be:[...](./core-circuit-CircuitModulus.md) |
| [Circuit](./core-circuit-Circuit.md) | A type that creates a circuit from a tuple of outputs. This type represents a complete circuit instance, constructed from its output gates. The type parameter `Outputs`[...](./core-circuit-Circuit.md) |
| [CircuitInput](./core-circuit-CircuitInput.md) | Defines an input for a circuit. Represents an input signal in the circuit, indexed by `N` . Each input must be assigned a value before circuit evaluation.[...](./core-circuit-CircuitInput.md) |
