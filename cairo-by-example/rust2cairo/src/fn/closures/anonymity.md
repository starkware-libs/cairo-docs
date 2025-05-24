# Type anonymity

Closures succinctly capture variables from enclosing scopes. Does this have
any consequences? It surely does. Observe how using a closure as a function
parameter requires [generics], which is necessary because of how they are
defined:

```cairo
{{#include ../../../listings/functions/closures/anonymity/src/lib.cairo:foo}}
```

When a closure is defined, the compiler implicitly creates a new
anonymous structure to store the captured variables inside, meanwhile
implementing the functionality via one of the `traits`: `Fn` or `FnOnce` for
this unknown type. This type is assigned to the variable which
is stored until calling.

Since this new type is of unknown type, any usage in a function will require
generics. However, an unbounded type parameter `<T>` would still be ambiguous
and not be allowed. Thus, bounding by one of the `traits`: `Fn` or `FnOnce`
(which it implements) is sufficient to specify its type.
Additional bounds are required to ensure that the closure can be called:

- `F` must implement `Drop` (or `Destruct`) to go out of scope
- `func::Output`, the output type of the closure, must implement `Drop`, as it is not used in the following code

```cairo,editable
{{#include ../../../listings/functions/closures/anonymity/src/lib.cairo:main}}
```

### See also:

[A thorough analysis][thorough_analysis], [`Fn`][fn], and [`FnOnce`][fnonce]

[generics]: ../../generics.md
[fn]: https://docs.swmansion.com/scarb/corelib/core-ops-function-Fn.html
[fnonce]: https://docs.swmansion.com/scarb/corelib/core-ops-function-FnOnce.html
