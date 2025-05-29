# u384

A 384-bit unsigned integer, used for circuit values.

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[u384](./core-circuit-u384.md)

<pre><code class="language-cairo">#[derive(Copy, Drop, Debug, PartialEq)]
pub struct u384 {
    pub limb0: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a>,
    pub limb1: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a>,
    pub limb2: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a>,
    pub limb3: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a>,
}</code></pre>

## Members

### limb0

The least significant 96 bits

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[u384](./core-circuit-u384.md)::[limb0](./core-circuit-u384.md#limb0)

<pre><code class="language-cairo">pub limb0: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a></code></pre>


### limb1

Bits 96-191

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[u384](./core-circuit-u384.md)::[limb1](./core-circuit-u384.md#limb1)

<pre><code class="language-cairo">pub limb1: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a></code></pre>


### limb2

Bits 192-287

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[u384](./core-circuit-u384.md)::[limb2](./core-circuit-u384.md#limb2)

<pre><code class="language-cairo">pub limb2: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a></code></pre>


### limb3

The most significant 96 bits

Fully qualified path: [core](./core.md)::[circuit](./core-circuit.md)::[u384](./core-circuit-u384.md)::[limb3](./core-circuit-u384.md#limb3)

<pre><code class="language-cairo">pub limb3: <a href="core-internal-bounded_int-BoundedInt.html">BoundedInt&lt;0, 79228162514264337593543950335&gt;</a></code></pre>


