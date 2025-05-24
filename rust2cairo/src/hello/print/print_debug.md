# Debug

All types which want to use `core::fmt` formatting `traits` require an
implementation to be printable. Automatic implementations are only provided
for types such as in the core library. All others _must_ be manually
implemented somehow.

The `fmt::Debug` `trait` makes this very straightforward. _All_ types can
`derive` (automatically create) the `fmt::Debug` implementation. This is
not true for `fmt::Display` which must be manually implemented.

```cairo
// This structure cannot be printed with `fmt::Display` or
// with `fmt::Debug` by default.
struct UnPrintable {
    value: i32
}

// The `derive` attribute automatically creates the implementation
// required to make this `struct` printable with `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable {
    value: i32
}
```

All `core` library types are automatically printable with `{:?}` too:

```cairo,editable
{{#include ../../../listings/hello/print/print_debug/src/lib.cairo}}
```

So `fmt::Debug` definitely makes this printable but sacrifices some elegance.

### Activities

- Try removing the `Debug` derive from one of the structs and see what error you get
- Add a new field to the `Person` struct and see how it appears in the debug output
- Try implementing `Display` for one of the structs to control its output format

### See also:

[`derive`][derive], [`core::fmt`][fmt], and [`struct`][structs]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[structs]: ../../custom_types/structs.md
