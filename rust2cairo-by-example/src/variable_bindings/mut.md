# Mutability

Variable bindings are immutable by default, but this can be overridden using
the `mut` modifier.

```cairo,editable
{{#include ../../listings/variable_bindings/mut_listing/src/lib.cairo}}
```

The compiler will throw a detailed diagnostic about mutability errors.
