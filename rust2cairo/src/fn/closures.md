# Closures

Closures are functions that can capture the enclosing environment. For example, a closure that captures the `x` variable:

```cairo, noplayground
|val| val + x
```

The syntax and capabilities of closures make them very convenient for on-the-fly usage. Calling a closure is exactly like calling a function. However, both input and return types _can_ be inferred and input variable names _must_ be specified.

Other characteristics of closures include:

- using `||` instead of `()` around input variables.
- optional body delimitation (`{}`) for a single line expression (mandatory otherwise).
- the ability to capture the outer environment variables.

```cairo,editable
{{#include ../../listings/functions/closures/src/lib.cairo}}
```
