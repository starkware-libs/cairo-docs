# CircuitModulus

A type that can be used as a circuit modulus (a u384 that is not zero or one).The modulus defines the finite field over which the circuit operates. It must be: - A 384-bit number (represented as four 96-bit limbs) - Not zero or one - Typically a prime number for cryptographic applications

Fully qualified path: `core::circuit::CircuitModulus`

<pre><code class="language-rust">pub extern type CircuitModulus</code></pre>

