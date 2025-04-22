# Input functions

Since closures may be used as arguments, you might wonder if the same can be said
about functions. Unfortunately, not (yet!).

```cairo,editable
{{#include ../../../listings/functions/closures/input_functions/src/lib.cairo}}
```

### See also:

[`Fn`][fn] and [`FnOnce`][fnonce]

[fn]: https://docs.swmansion.com/scarb/corelib/core-ops-function-Fn.html
[fnonce]: https://docs.swmansion.com/scarb/corelib/core-ops-function-FnOnce.html
