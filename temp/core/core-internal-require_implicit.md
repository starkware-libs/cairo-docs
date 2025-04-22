# require_implicit

Function to enforce that `Implicit` is used by a function calling it. Note: This extern function is not mapped to a Sierra function, and all usages of it are removed during compilation.

Fully qualified path: `core::internal::require_implicit`

```rust
pub extern fn require_implicit<Implicit>() implicits(Implicit) nopanic;
```

