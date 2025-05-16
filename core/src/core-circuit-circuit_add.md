# circuit_add

Creates a new circuit element representing addition modulo p of two input circuits.This function combines two circuit elements using modular addition, creating a new circuit element that represents their sum modulo the circuit's modulus.  # Arguments`lhs` - Left-hand side circuit element * `rhs` - Right-hand side circuit element  # ReturnsA new circuit element representing `(lhs + rhs) mod p`  # Examples
```cairo
let a = CircuitElement::<CircuitInput<0>> {};
let b = CircuitElement::<CircuitInput<1>> {};
let sum = circuit_add(a, b);
```

Fully qualified path: `core::circuit::circuit_add`

<pre><code class="language-rust">pub fn circuit_add&lt;Lhs, Rhs, +CircuitElementTrait&lt;Lhs&gt;, +CircuitElementTrait&lt;Rhs&gt;&gt;(
    lhs: CircuitElement&lt;Lhs&gt;, rhs: CircuitElement&lt;Rhs&gt;,
) -&gt; CircuitElement&lt;AddModGate&lt;Lhs, Rhs&gt;&gt;</code></pre>

