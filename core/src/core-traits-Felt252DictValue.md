# Felt252DictValue

A trait that must be implemented for any type that will be stored as a value in a `Felt252Dict`.
When working with dictionaries in Cairo, we need a way to represent "empty" or "uninitialized"
slots. This trait provides a zero-like default value that is returned when accessing a key
that hasn't been explicitly set.
# Why is this needed?

The `Felt252Dict` implementation needs to handle cases where a key hasn't been assigned a value
yet.
Instead of using `Option` or similar constructs, it uses a zero-like value specific to each
type.
This trait is only implemented for primitive scalar types and `Nullable<T>`. It cannot be
implemented manually.
Instead, if you want to use a custom type as a value in a dictionary, you can wrap your type in
a [`Nullable`](./core-nullable-Nullable.md), which implements `Felt252DictValue` for any wrapped type.
# Examples

```cairo
use core::dict::Felt252Dict;

#[derive(Copy, Drop, Default)]
struct Counter {
    value: u32,
}

 // u8 already implements Felt252DictValue
 let mut dict: Felt252Dict<u8> = Default::default();
 assert!(dict.get(123) == 0);

 // Counter is wrapped in a Nullable, as it doesn't implement Felt252DictValue
 let mut counters: Felt252Dict<Nullable<Counter>> = Default::default();

 // If the key is not set, `deref` would panic. `deref_or` returns the default value.
 let maybe_counter: Nullable<Counter> = counters.get(123);
 assert!(maybe_counter.deref_or(Default::default()).value == 0);
```

Fully qualified path: [core](./core.md)::[traits](./core-traits.md)::[Felt252DictValue](./core-traits-Felt252DictValue.md)

<pre><code class="language-cairo">pub trait Felt252DictValue&lt;T&gt;</code></pre>

## Trait functions

### zero_default

Returns the default value for this type when used in a `Felt252Dict`.
This value should be logically equivalent to zero or an "empty" state.

Fully qualified path: [core](./core.md)::[traits](./core-traits.md)::[Felt252DictValue](./core-traits-Felt252DictValue.md)::[zero_default](./core-traits-Felt252DictValue.md#zero_default)

<pre><code class="language-cairo">fn zero_default&lt;T, T&gt;() -&gt; T</code></pre>


