# OptionRev

Same as `Option`, except that the order of the variants is reversed. This is used as the return type of some libfuncs for efficiency reasons.

Fully qualified path: `core::internal::OptionRev`

<pre><code class="language-rust">#[must_use]
#[derive(Copy, Drop, Debug, PartialEq)]
pub enum OptionRev&lt;T&gt; {
    None,
    Some: T,
}</code></pre>

## Variants

### None

Fully qualified path: `core::internal::OptionRev::None`

<pre><code class="language-rust">None</code></pre>


### Some

Fully qualified path: `core::internal::OptionRev::Some`

<pre><code class="language-rust">Some : T</code></pre>


