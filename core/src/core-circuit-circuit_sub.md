# circuit_sub

Creates a new circuit element representing subtraction modulo p of two input circuits.This function combines two circuit elements using modular subtraction, creating a new circuit element that represents their difference modulo the circuit's modulus.  # Arguments`lhs` - Left-hand side circuit element (minuend) * `rhs` - Right-hand side circuit element (subtrahend)  # ReturnsA new circuit element representing `(lhs - rhs) mod p`  # Examples
```cairo
let a = CircuitElement::<CircuitInput<0>> {};
let b = CircuitElement::<CircuitInput<1>> {};
let diff = circuit_sub(a, b);
```

Fully qualified path: `core::circuit::circuit_sub`

<pre><code class="language-rust">pub fn circuit_sub&lt;Lhs, Rhs, +CircuitElementTrait&lt;Lhs&gt;, +CircuitElementTrait&lt;Rhs&gt;&gt;(
    lhs: CircuitElement&lt;Lhs&gt;, rhs: CircuitElement&lt;Rhs&gt;,
) -&gt; CircuitElement&lt;SubModGate&lt;Lhs, Rhs&gt;&gt;</code></pre>

