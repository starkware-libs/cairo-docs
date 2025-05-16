# cheatcode

A general cheatcode function used to simplify implementation of Starknet testing functions.This is the base function used by testing utilities to interact with the test environment. External users can implement custom cheatcodes by injecting a custom `CairoHintProcessor` in the runner.  # Arguments`selector` - The cheatcode identifier. `input` - Input parameters for the cheatcode.  # ReturnsA span containing the cheatcode's output

Fully qualified path: `core::starknet::testing::cheatcode`

<pre><code class="language-rust">pub extern fn cheatcode&lt;const selector: felt252&gt;(
    input: Span&lt;felt252&gt;,
) -&gt; Span&lt;felt252&gt; implicits() nopanic;</code></pre>

