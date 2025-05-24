# Ownership and moves

Because Cairo uses a linear type system, values must be used exactly once. This means that when passing function arguments (`foo(x)`), the value is _moved_ from one variable to another. After a value is moved, the previous variable can no longer be used.

This is similar to Rust's ownership system, but for different reasons. While Rust's ownership prevents data races and memory safety issues, Cairo's linear type system ensures code provability and abstracts the VM's immutable memory model.

```cairo,editable
{{#include ../../listings/scope/move_listing/src/lib.cairo}}
```
