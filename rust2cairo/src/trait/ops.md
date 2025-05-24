# Operator Overloading

In Cairo, many operators can be overloaded via traits. That is, some operators can be used to accomplish different tasks based on their input arguments. This is possible because operators are syntactic sugar for method calls. For example, the `+` operator in `a + b` calls the `add` method (as in `a.add(b)`). This `add` method is part of the `Add` trait. Hence, the `+` operator can be used by any implementor of the `Add` trait.

A list of the traits that overload operators can be found in [`core::ops`][ops] and [`core::traits`][core-traits].

```cairo,editable
{{#include ../../listings/trait_listing/ops/src/lib.cairo}}
```

### See Also

[Add][add], [Operators][ops]

[core-traits]: https://docs.swmansion.com/scarb/corelib/core-traits.html
[add]: https://docs.swmansion.com/scarb/corelib/core-traits-Add.html
[ops]: https://docs.swmansion.com/scarb/corelib/core-ops.html
