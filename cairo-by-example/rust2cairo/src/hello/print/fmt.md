# Formatting

Specifying formatting via a format string in Cairo is similar to [Rust](https://doc.rust-lang.org/rust-by-example/hello/print/fmt.html), except that the `{:o}` string is not supported:

<!-- > You can view a full list of formatting traits and their argument types in the [`core::fmt` documentation][fmt_traits]. -->

```cairo,editable
{{#include ../../../listings/hello/print/fmt/src/lib.cairo}}
```

### See also:

[`core::fmt`][fmt]

[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[fmt_traits]: https://docs.swmansion.com/scarb/corelib/core-fmt.html#traits
