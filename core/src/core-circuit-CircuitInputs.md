# CircuitInputs

Fully qualified path: `core::circuit::CircuitInputs`

<pre><code class="language-rust">pub trait CircuitInputs&lt;CES&gt;</code></pre>

## Trait functions

### new_inputs

Initializes a new circuit instance with inputs.This function creates a new input accumulator for the circuit, which can then be used to add input values sequentially.  # ReturnsAn `AddInputResult` that can be used to add input values to the circuit

Fully qualified path: `core::circuit::CircuitInputs::new_inputs`

<pre><code class="language-rust">fn new_inputs&lt;impl CD: CircuitDefinition&lt;CES&gt;, +Drop&lt;CES&gt;&gt;(
    self: CES,
) -&gt; AddInputResult&lt;CD::CircuitType&gt;</code></pre>


