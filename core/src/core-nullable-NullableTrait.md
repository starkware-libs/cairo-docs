# NullableTrait

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)

<pre><code class="language-cairo">pub trait NullableTrait&lt;T&gt;</code></pre>

## Trait functions

### deref

Wrapper for `Deref::deref`. Prefer using `Deref::deref` directly.
This function exists for backwards compatibility.
# Examples

Preferred way:
```cairo
let value: Nullable<u32> = NullableTrait::new(42);
let unwrapped = value.deref();
```

This function method does the same thing:
```cairo
use core::nullable::NullableTrait;
let also_unwrapped = NullableTrait::deref(value);
```

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)::[deref](./core-nullable-NullableTrait.md#deref)

<pre><code class="language-cairo">fn deref&lt;T, T&gt;(nullable: Nullable&lt;T&gt;) -&gt; T</code></pre>


### deref_or

Returns the contained value if not null, or returns the provided default value.
# Examples

```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(value.deref_or(0) == 42);

let null_value: Nullable<u32> = Default::default();
assert!(null_value.deref_or(0) == 0);
```

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)::[deref_or](./core-nullable-NullableTrait.md#deref_or)

<pre><code class="language-cairo">fn deref_or&lt;T, T, +Drop&lt;T&gt;&gt;(self: Nullable&lt;T&gt;, default: T) -&gt; T</code></pre>


### new

Creates a new non-null `Nullable` with the given value.
# Examples

```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(!value.is_null());
```

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)::[new](./core-nullable-NullableTrait.md#new)

<pre><code class="language-cairo">fn new&lt;T, T&gt;(value: T) -&gt; <a href="core-nullable-Nullable.html">Nullable&lt;T&gt;</a></code></pre>


### is_null

Returns `true` if the value is null.
# Examples

```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(!value.is_null());

let null_value: Nullable<u32> = Default::default();
assert!(null_value.is_null());
```

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)::[is_null](./core-nullable-NullableTrait.md#is_null)

<pre><code class="language-cairo">fn is_null&lt;T, T&gt;(self: @Nullable&lt;T&gt;) -&gt; <a href="core-bool.html">bool</a></code></pre>


### as_snapshot

Creates a new `Nullable` containing a snapshot of the value.
This is useful when working with non-copyable types inside a `Nullable`.
This allows you to keep using the original value while also having access to a
snapshot of it, preventing the original value from being moved.
# Examples

```cairo
let value: Nullable<Array<u32>> = NullableTrait::new(array![1, 2, 3]);
let res = (@value).as_snapshot();
assert!(res.deref() == @array![1, 2, 3]);
assert!(value.deref() == array![1, 2, 3]);
```

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)::[NullableTrait](./core-nullable-NullableTrait.md)::[as_snapshot](./core-nullable-NullableTrait.md#as_snapshot)

<pre><code class="language-cairo">fn as_snapshot&lt;T, T&gt;(self: @Nullable&lt;T&gt;) -&gt; <a href="core-nullable-Nullable.html">Nullable&lt;@T&gt;</a></code></pre>


