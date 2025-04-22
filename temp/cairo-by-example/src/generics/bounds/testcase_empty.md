# Testcase: empty bounds

A consequence of how bounds work is that even if a `trait` doesn't include any functionality, you can still use it as a bound. `Drop` and `Copy` are examples of such `trait`s from the `core` library.

```cairo, editable
{{#include ../../../listings/generics/bounds/testcase_empty/src/lib.cairo}}
```

### See also:

[`core::traits::Drop`][drop], [`core::traits::Copy`][copy], and [`trait`s][traits]

[drop]: https://docs.swmansion.com/scarb/corelib/core-traits-Drop.html
[copy]: https://docs.swmansion.com/scarb/corelib/core-traits-Copy.html
[traits]: ../../trait.md
