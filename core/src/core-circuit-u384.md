# u384

A 384-bit unsigned integer, used for circuit values.

Fully qualified path: `core::circuit::u384`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug, PartialEq)]
pub struct u384 {
    pub limb0: u96,
    pub limb1: u96,
    pub limb2: u96,
    pub limb3: u96,
}</code></pre>

## Members

### limb0

The least significant 96 bits

Fully qualified path: `core::circuit::u384::limb0`

<pre><code class="language-rust">pub limb0: u96</code></pre>


### limb1

Bits 96-191

Fully qualified path: `core::circuit::u384::limb1`

<pre><code class="language-rust">pub limb1: u96</code></pre>


### limb2

Bits 192-287

Fully qualified path: `core::circuit::u384::limb2`

<pre><code class="language-rust">pub limb2: u96</code></pre>


### limb3

The most significant 96 bits

Fully qualified path: `core::circuit::u384::limb3`

<pre><code class="language-rust">pub limb3: u96</code></pre>


