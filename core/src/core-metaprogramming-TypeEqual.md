# TypeEqual

A trait that can be used to disable implementations based on the types of the generic args. Assumes that `TypeEqualImpl<T>` is the only implementation of this trait.Primarily used for optimizations by enabling type-specific implementations. Since `TypeEqualImpl<T>` is the only implementation, adding `-TypeEqual<T, U>` as a trait bound ensures the implementation is only available when T and U are different types.

Fully qualified path: `core::metaprogramming::TypeEqual`

<pre><code class="language-rust">pub trait TypeEqual&lt;S, T&gt;</code></pre>

