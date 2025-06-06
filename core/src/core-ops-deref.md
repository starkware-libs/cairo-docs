# deref

Dereferencing traits for transparent access to wrapped values.
This module provides traits that enable accessing the content of wrapped types
as if they were the inner type directly. This is particularly useful for:
- Smart pointers and wrapper types (e.g., `Box<T>`)
- Nested data structures
- Enum variants sharing common fields
# Core Traits

- [`Deref`](./core-ops-deref-Deref.md): Provides read-only access to the wrapped value
- [`DerefMut`](./core-ops-deref-DerefMut.md): Provides read-only access to the wrapped value in mutable contexts
# Examples

```cairo
// Accessing nested struct fields through deref
#[derive(Drop, Copy)]
struct Inner { value: felt252 }

#[derive(Drop, Copy)]
struct Outer { inner: Inner }

impl OuterDeref of Deref<Outer> {
    type Target = Inner;
    fn deref(self: Outer) -> Inner { self.inner }
}

let outer = Outer { inner: Inner { value: 42 } };
assert!(outer.value == 42); // Access Inner's field directly
```

Fully qualified path: [core](./core.md)::[ops](./core-ops.md)::[deref](./core-ops-deref.md)


[Traits](./core-ops-deref-traits.md)
 ---
| | |
|:---|:---|
| [Deref](./core-ops-deref-Deref.md) | A trait for dereferencing a value to provide transparent access to its contents. Implementing this trait allows a type to behave like its inner type, enabling direct access to[...](./core-ops-deref-Deref.md) |
| [DerefMut](./core-ops-deref-DerefMut.md) | A trait for dereferencing in mutable contexts. This trait is similar to `Deref`  but specifically handles cases where the value accessed is mutable. Despite its name, `DerefMut`[...](./core-ops-deref-DerefMut.md) |
