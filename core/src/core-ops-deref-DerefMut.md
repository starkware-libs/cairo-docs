# DerefMut

A trait for dereferencing in mutable contexts.This trait is similar to `Deref` but specifically handles cases where the value accessed is mutable. Despite its name, `DerefMut` does NOT allow modifying the inner value - it only indicates that the container itself is mutable.  # Examples
```cairo
#[derive(Copy, Drop)]
struct MutWrapper<T> {
    value: T
}

impl MutWrapperDerefMut<T, +Copy<T>> of DerefMut<MutWrapper<T>> {
    type Target = T;
    fn deref_mut(ref self: MutWrapper<T>) -> T {
        self.value
    }
}

// This will work since x is mutable
let mut x = MutWrapper { value: 42 };
let val = x.deref_mut();
assert!(val == 42);

// This would fail to compile since y is not mutable
let y = MutWrapper { value: 42 };
let val = y.deref_mut(); // Compile error
```

Fully qualified path: `core::ops::deref::DerefMut`

<pre><code class="language-rust">pub trait DerefMut&lt;T&gt;</code></pre>

## Trait functions

### deref_mut

Returns the dereferenced value.

Fully qualified path: `core::ops::deref::DerefMut::deref_mut`

<pre><code class="language-rust">fn deref_mut(ref self: T) -&gt; Self::Target</code></pre>


## Trait types

### Target

The type of the dereferenced value.

Fully qualified path: `core::ops::deref::DerefMut::Target`

<pre><code class="language-rust">type Target;</code></pre>


