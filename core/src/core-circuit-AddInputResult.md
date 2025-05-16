# AddInputResult

The result of filling an input in the circuit instance's data.This enum represents the state of input filling process, indicating whether all inputs have been provided or more are needed.

Fully qualified path: `core::circuit::AddInputResult`

<pre><code class="language-rust">pub enum AddInputResult&lt;C&gt; {
    Done: CircuitData&lt;C&gt;,
    More: CircuitInputAccumulator&lt;C&gt;,
}</code></pre>

## Variants

### Done

All inputs have been filled and the circuit data is complete.

Fully qualified path: `core::circuit::AddInputResult::Done`

<pre><code class="language-rust">Done : CircuitData &lt; C &gt;</code></pre>


### More

More inputs are needed to complete the circuit instance's data.

Fully qualified path: `core::circuit::AddInputResult::More`

<pre><code class="language-rust">More : CircuitInputAccumulator &lt; C &gt;</code></pre>


