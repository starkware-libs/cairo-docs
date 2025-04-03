# `TryInto` for Fallible Conversions

The [`TryInto`] trait is used for conversions that might fail. For example, converting from a larger integer type to a smaller one, or parsing a string into a number.

Unlike Rust which uses Result for fallible operations, Cairo uses [`Option`] to represent operations that might fail.

```cairo
{{#include ../../listings/conversion/try_into_1/src/lib.cairo}}
```

[`TryInto`]: https://docs.swmansion.com/scarb/corelib/core-traits-TryInto.html
[`Option`]: https://docs.swmansion.com/scarb/corelib/core-option-Option.html
