# Formatting

We've seen that formatting is specified via a _format string_:

- `format!("{}", foo)` -> `"3735928559"`
- `format!("{:x}", foo)` -> [`"0xdeadbeef"`][deadbeef]

The same variable (`foo`) can be formatted differently depending on which
_argument type_ is used: `x` vs _unspecified_.

This formatting functionality is implemented via traits, and there is one trait
for each argument type. The most common formatting trait is `Display`, which
handles cases where the argument type is left unspecified: `{}` for instance.

```cairo,editable
{{#include ../../../listings/hello/print/fmt/src/lib.cairo}}
```

You can view a [full list of formatting traits][fmt_traits] and their argument
types in the [`core::fmt`][fmt] documentation.

### See also:

[`core::fmt`][fmt]

[deadbeef]: https://en.wikipedia.org/wiki/Deadbeef#Magic_debug_values
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[fmt_traits]: https://docs.swmansion.com/scarb/corelib/core-fmt.html#formatting-traits
