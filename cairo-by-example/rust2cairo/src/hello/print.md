# Formatted print

Printing in Cairo is handled similarly to [Rust](https://doc.rust-lang.org/rust-by-example/hello/print.html), except:

- [`macros`][macros] are defined in [`core::fmt`][fmt] instead of `std::fmt`
- `format!` writes formatted text to [`ByteArray`][bytearray] instead of `String`
- `eprint!` and `eprintln!` are not supported

```cairo,editable
{{#include ../../listings/hello/print/src/lib.cairo}}
```

### Activities

- Fix the issue in the above code (see FIXME) so that it runs without
  error.
- Try uncommenting the line that attempts to format the `Structure` struct
  (see TODO)

### See also:

[`std::fmt`][fmt], [`macros`][macros], [`struct`][structs], [`traits`][traits]

[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
[bytearray]: ../core/bytearrays.md
[structs]: ../custom_types/structs.md
[traits]: https://docs.swmansion.com/scarb/corelib/core-fmt.html#traits
[attribute]: ../attribute.md
