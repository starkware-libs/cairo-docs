# PanicDestruct

A trait that allows for destruction of a value in case of a panic.This trait is automatically implemented from the `Destruct` implementation for a type.

Fully qualified path: `core::traits::PanicDestruct`

<pre><code class="language-rust">pub trait PanicDestruct&lt;T&gt;</code></pre>

## Trait functions

### panic_destruct

Fully qualified path: `core::traits::PanicDestruct::panic_destruct`

<pre><code class="language-rust">fn panic_destruct(self: T, ref panic: Panic) nopanic</code></pre>


