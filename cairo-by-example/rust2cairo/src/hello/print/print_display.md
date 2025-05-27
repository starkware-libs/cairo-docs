# Display

`fmt::Display` in Cairo is identical to [Rust](https://doc.rust-lang.org/rust-by-example/hello/print/print_display.html):

```cairo, editable
{{#include ../../../listings/hello/print/print_display/src/lib.cairo:main}}
```

### Activity

After checking the output of the above example, use the `Point2D` struct as a guide to add a `Complex` struct to the example. When printed in the same way, the output should be:

```txt
Display: 3 + 7i
Debug: Complex { real: 3, imag: 7 }
```

### See also:

[`derive`][derive], [`core::fmt`][fmt], [`macros`][macros], [`struct`][structs],
[`trait`][traits], and [`use`][use]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
[structs]: ../../custom_types/structs.md
[traits]: ../../trait.md
[use]: ../../mod/use.md
