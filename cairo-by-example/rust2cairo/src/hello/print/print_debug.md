# Debug

`fmt::Debug` in Cairo is identical to [Rust](https://doc.rust-lang.org/rust-by-example/hello/print/print_debug.html):

```cairo,editable
{{#include ../../../listings/hello/print/print_debug/src/lib.cairo}}
```

### Activities

- Try removing the `Debug` derive from one of the structs and see what error you get
- Add a new field to the `Person` struct and see how it appears in the debug output
- Try implementing `Display` for one of the structs to control its output format

### See also:

[`derive`][derive], [`core::fmt`][fmt], and [`struct`][structs]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[structs]: ../../custom_types/structs.md
