# Type Conversion with `Into`

In Cairo, type conversions are primarily handled through the [`Into`] trait. This trait allows you to define how to convert one type into another.

## Converting Between Types

The [`Into`] trait provides a mechanism for converting between several types. There are numerous implementations of this trait within the core library for conversion of primitive and common types.

For example, we can easily convert a `u8` into a `u16`:

```cairo
{{#include ../../listings/conversion/into_1/src/lib.cairo}}
```

We can do something similar for defining a conversion for our own type.

```cairo
{{#include ../../listings/conversion/into_2/src/lib.cairo}}
```

[`Into`]: https://docs.swmansion.com/scarb/corelib/core-traits-Into.html
