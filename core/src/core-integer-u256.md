# u256

The 256-bit unsigned integer type.The `u256` type is composed of two 128-bit parts: the low part [0, 128) and the high part [128, 256).

Fully qualified path: `core::integer::u256`

<pre><code class="language-rust">#[derive(Copy, Drop, Hash, PartialEq, Serde)]
pub struct u256 {
    pub low: u128,
    pub high: u128,
}</code></pre>

## Members

### low

Fully qualified path: `core::integer::u256::low`

<pre><code class="language-rust">pub low: u128</code></pre>


### high

Fully qualified path: `core::integer::u256::high`

<pre><code class="language-rust">pub high: u128</code></pre>


