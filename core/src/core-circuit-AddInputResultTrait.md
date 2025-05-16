# AddInputResultTrait

Fully qualified path: `core::circuit::AddInputResultTrait`

<pre><code class="language-rust">pub trait AddInputResultTrait&lt;C&gt;</code></pre>

## Trait functions

### next

Adds an input value to the circuit instance.  # Arguments`value` - The value to add as input, must be convertible to circuit input value  # ReturnsA new `AddInputResult` that can be used to add more inputs or finalize  # PanicsPanics if all inputs have already been filled

Fully qualified path: `core::circuit::AddInputResultTrait::next`

<pre><code class="language-rust">fn next&lt;Value, +IntoCircuitInputValue&lt;Value&gt;, +Drop&lt;Value&gt;&gt;(
    self: AddInputResult&lt;C&gt;, value: Value,
) -&gt; AddInputResult&lt;C&gt;</code></pre>


### done

Finalizes the input process and returns the circuit data.  # ReturnsThe complete circuit data ready for evaluation  # PanicsPanics if not all required inputs have been filled

Fully qualified path: `core::circuit::AddInputResultTrait::done`

<pre><code class="language-rust">fn done(self: AddInputResult&lt;C&gt;) -&gt; CircuitData&lt;C&gt;</code></pre>


