# As input parameters

While Cairo chooses how to capture variables on the fly mostly without type
annotation, this ambiguity is not allowed when writing functions. When
taking a closure as an input parameter, the closure's complete type must be
annotated using one of two `traits`, and they're determined by what the
closure does with captured value. In order of decreasing restriction,
they are:

- `Fn`: the closure uses the captured value by snapshot (`@T`)
- `FnOnce`: the closure uses the captured value by value (`T`)

On a variable-by-variable basis, the compiler will capture variables in the
least restrictive manner possible.

For instance, consider a parameter annotated as `FnOnce`. This specifies
that the closure _may_ capture by `@T` or `T`, but the compiler
will ultimately choose based on how the captured variables are used in the
closure.

This is because if a move is possible, then any type of snapshot should also
be possible. Note that the reverse is not true. If the parameter is
annotated as `Fn`, then capturing variables by `T` is not allowed.
However, `@T` is allowed.

In the following example, try swapping the usage of `Fn` and `FnOnce` to see what happens:

> Note: Cairo 2.11 provides an experimental feature allowing you to specify the associated type of trait, using `experimental-features = ["associated_item_constraints"]` in your `Scarb.toml`.

```cairo,editable
{{#include ../../../listings/functions/closures/input_parameters/src/lib.cairo}}
```

### See also:

[`Fn`][fn], [Generics][generics], and [`FnOnce`][fnonce]

[fn]: https://docs.swmansion.com/scarb/corelib/core-ops-function-Fn.html
[fnonce]: https://docs.swmansion.com/scarb/corelib/core-ops-function-FnOnce.html
[generics]: ../../generics.md
