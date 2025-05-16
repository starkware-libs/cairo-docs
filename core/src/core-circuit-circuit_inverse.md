# circuit_inverse

Creates a new circuit element representing the multiplicative inverse modulo p of an input circuit.This function creates a new circuit element representing the multiplicative inverse of the input element modulo the circuit's modulus. The operation will fail during evaluation if the input is not invertible (not coprime with the modulus).  # Arguments`input` - Circuit element to compute the inverse of  # ReturnsA new circuit element representing `input^(-1) mod p`  # Examples
```cairo
let a = CircuitElement::<CircuitInput<0>> {};
let inv_a = circuit_inverse(a);
```

Fully qualified path: `core::circuit::circuit_inverse`

<pre><code class="language-rust">pub fn circuit_inverse&lt;Input, +CircuitElementTrait&lt;Input&gt;&gt;(
    input: CircuitElement&lt;Input&gt;,
) -&gt; CircuitElement&lt;InverseGate&lt;Input&gt;&gt;</code></pre>

