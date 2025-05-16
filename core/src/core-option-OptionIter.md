# OptionIter

An iterator over the value in the [`Some`](./core-option.md#some) variant of an [`Option`](./core-option-Option.md).The iterator yields one value if the [`Option`](./core-option-Option.md) is a [`Some`](./core-option.md#some), otherwise none.This struct is created by the [`into_iter`](`into_iter`) method on [`Option`](./core-option-Option.md) (provided by the [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md) trait).

Fully qualified path: `core::option::OptionIter`

<pre><code class="language-rust">#[derive(Drop)]
pub struct OptionIter&lt;T&gt; {
    inner: Option&lt;T&gt;,
}</code></pre>

