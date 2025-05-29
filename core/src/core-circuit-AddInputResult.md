# AddInputResult

The result of filling an input in the circuit instance's data.
This enum represents the state of input filling process, indicating whether
all inputs have been provided or more are needed.

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResult](./core-circuit-AddInputResult.md)

<pre><code class="language-cairo">pub enum AddInputResult {
    Done: <a href="core-circuit-CircuitData.html">CircuitData&lt;C&gt;</a>,
    More: <a href="core-circuit-CircuitInputAccumulator.html">CircuitInputAccumulator&lt;C&gt;</a>,
}</code></pre>

## Variants

### Done

All inputs have been filled and the circuit data is complete.

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResult](./core-circuit-AddInputResult.md)::[Done](./core-circuit-AddInputResult.md#done)

<pre><code class="language-cairo">Done: <a href="core-circuit-CircuitData.html">CircuitData&lt;C&gt;</a></code></pre>


### More

More inputs are needed to complete the circuit instance's data.

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[AddInputResult](./core-circuit-AddInputResult.md)::[More](./core-circuit-AddInputResult.md#more)

<pre><code class="language-cairo">More: <a href="core-circuit-CircuitInputAccumulator.html">CircuitInputAccumulator&lt;C&gt;</a></code></pre>


