# circuit_mul

Creates a new circuit element representing multiplication modulo p of two input circuits.This function combines two circuit elements using modular multiplication, creating a new circuit element that represents their product modulo the circuit's modulus.  # Arguments`lhs` - Left-hand side circuit element * `rhs` - Right-hand side circuit element  # ReturnsA new circuit element representing `(lhs * rhs) mod p`  # Examples
```cairo
let a = CircuitElement::<CircuitInput<0>> {};
let b = CircuitElement::<CircuitInput<1>> {};
let product = circuit_mul(a, b);
```

Fully qualified path: `core::circuit::circuit_mul`

<pre><code class="language-rust">pub fn circuit_mul&lt;Lhs, Rhs, +CircuitElementTrait&lt;Lhs&gt;, +CircuitElementTrait&lt;Rhs&gt;&gt;(
    lhs: CircuitElement&lt;Lhs&gt;, rhs: CircuitElement&lt;Rhs&gt;,
) -&gt; CircuitElement&lt;MulModGate&lt;Lhs, Rhs&gt;&gt;</code></pre>

