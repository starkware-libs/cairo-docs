# EcStateTrait

Fully qualified path: `core::ec::EcStateTrait`

<pre><code class="language-rust">pub trait EcStateTrait</code></pre>

## Trait functions

### init

Initializes an EC computation with the zero point.  # Examples
```cairo
let mut state = EcStateTrait::init();
```

Fully qualified path: `core::ec::EcStateTrait::init`

<pre><code class="language-rust">fn init() -&gt; EcState nopanic</code></pre>


### add

Adds a point to the computation.  # Arguments`p` - The non-zero point to add

Fully qualified path: `core::ec::EcStateTrait::add`

<pre><code class="language-rust">fn add(ref self: EcState, p: NonZeroEcPoint) nopanic</code></pre>


### sub

Subtracts a point to the computation.  # Arguments`p` - The non-zero point to subtract

Fully qualified path: `core::ec::EcStateTrait::sub`

<pre><code class="language-rust">fn sub(ref self: EcState, p: NonZeroEcPoint)</code></pre>


### add_mul

Adds the product `p * scalar` to the state.  # Arguments`scalar` - The scalar to multiply the point by * `p` - The non-zero point to multiply and add

Fully qualified path: `core::ec::EcStateTrait::add_mul`

<pre><code class="language-rust">fn add_mul(ref self: EcState, scalar: felt252, p: NonZeroEcPoint) nopanic</code></pre>


### finalize_nz

Finalizes the EC computation and returns the result as a non-zero point.  # Returns`Option<NonZeroEcPoint>` - The resulting point, or None if the result is the zero point  # PanicsPanics if the result is the point at infinity.

Fully qualified path: `core::ec::EcStateTrait::finalize_nz`

<pre><code class="language-rust">fn finalize_nz(self: EcState) -&gt; Option&lt;NonZeroEcPoint&gt; nopanic</code></pre>


### finalize

Finalizes the EC computation and returns the result.Returns the zero point if the computation results in the point at infinity.

Fully qualified path: `core::ec::EcStateTrait::finalize`

<pre><code class="language-rust">fn finalize(self: EcState) -&gt; EcPoint</code></pre>


