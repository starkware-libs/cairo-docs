# CircuitDefinition

A trait for defining a circuit's structure and behavior.This trait is used to define the structure of a circuit, including its inputs, gates, and outputs. It provides the foundation for circuit evaluation. The `CES` type parameter represents a tuple of `CircuitElement`s that together define the circuit's structure.

Fully qualified path: `core::circuit::CircuitDefinition`

<pre><code class="language-rust">pub trait CircuitDefinition&lt;CES&gt;</code></pre>

## Trait types

### CircuitType

The internal circuit type representing a tuple of `CircuitElement`s.

Fully qualified path: `core::circuit::CircuitDefinition::CircuitType`

<pre><code class="language-rust">type CircuitType;</code></pre>


