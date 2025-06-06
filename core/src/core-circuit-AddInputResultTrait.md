# AddInputResultTrait

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResultTrait](./core-circuit-AddInputResultTrait.md)

<pre><code class="language-cairo">pub trait AddInputResultTrait&lt;C&gt;</code></pre>

## Trait functions

### next

Adds an input value to the circuit instance.
# Arguments

- `value` - The value to add as input, must be convertible to circuit input value
# Returns

A new `AddInputResult` that can be used to add more inputs or finalize
# Panics

Panics if all inputs have already been filled

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResultTrait](./core-circuit-AddInputResultTrait.md)::[next](./core-circuit-AddInputResultTrait.md#next)

<pre><code class="language-cairo">fn next&lt;C, C, Value, +IntoCircuitInputValue&lt;Value&gt;, +Drop&lt;Value&gt;&gt;(
    self: AddInputResult&lt;C&gt;, value: Value,
) -&gt; <a href="core-circuit-AddInputResult.html">AddInputResult&lt;C&gt;</a></code></pre>


### done

Finalizes the input process and returns the circuit data.
# Returns

The complete circuit data ready for evaluation
# Panics

Panics if not all required inputs have been filled

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResultTrait](./core-circuit-AddInputResultTrait.md)::[done](./core-circuit-AddInputResultTrait.md#done)

<pre><code class="language-cairo">fn done&lt;C, C&gt;(self: AddInputResult&lt;C&gt;) -&gt; <a href="core-circuit-CircuitData.html">CircuitData&lt;C&gt;</a></code></pre>


