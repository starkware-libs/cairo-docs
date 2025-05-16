# Deref

A trait for dereferencing a value to provide transparent access to its contents.Implementing this trait allows a type to behave like its inner type, enabling direct access to the inner type's fields.Note: The `Deref` mechanism is limited and cannot be used to implicitly convert a type to its target type when passing arguments to functions. For example, if you have a function that takes an `Inner`, you cannot pass an `Outer` to it even if `Outer` implements `Deref`.  # Examples
```cairo
struct Wrapper<T> { inner: T }

impl WrapperDeref<T> of Deref<Wrapper<T>> {
    type Target = T;
    fn deref(self: Wrapper<T>) -> T { self.inner }
}

let wrapped = Wrapper { inner: 42 };
assert!(wrapped.deref() == 42);
```

Fully qualified path: `core::ops::deref::Deref`

<pre><code class="language-rust">pub trait Deref&lt;T&gt;</code></pre>

## Trait functions

### deref

Returns the dereferenced value.

Fully qualified path: `core::ops::deref::Deref::deref`

<pre><code class="language-rust">fn deref(self: T) -&gt; Self::Target</code></pre>


## Trait types

### Target

The type of the dereferenced value.

Fully qualified path: `core::ops::deref::Deref::Target`

<pre><code class="language-rust">type Target;</code></pre>


