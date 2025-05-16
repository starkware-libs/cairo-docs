# EvalCircuitTrait

Fully qualified path: `core::circuit::EvalCircuitTrait`

<pre><code class="language-rust">pub trait EvalCircuitTrait&lt;C&gt;</code></pre>

## Trait functions

### eval

Evaluates the circuit with the given modulus.  # Arguments`modulus` - The modulus to use for arithmetic operations  # ReturnsResult containing either the circuit outputs or a failure indication

Fully qualified path: `core::circuit::EvalCircuitTrait::eval`

<pre><code class="language-rust">fn eval(self: CircuitData&lt;C&gt;, modulus: CircuitModulus) -&gt; crate::circuit::EvalCircuitResult&lt;C&gt;</code></pre>


### eval_ex

Evaluates the circuit with an explicit descriptor and modulus.  # Arguments`descriptor` - The circuit descriptor * `modulus` - The modulus to use for arithmetic operations  # ReturnsResult containing either the circuit outputs or a failure indication

Fully qualified path: `core::circuit::EvalCircuitTrait::eval_ex`

<pre><code class="language-rust">fn eval_ex(
    self: CircuitData&lt;C&gt;, descriptor: CircuitDescriptor&lt;C&gt;, modulus: CircuitModulus,
) -&gt; crate::circuit::EvalCircuitResult&lt;C&gt;</code></pre>


