# Formatted print

Printing is handled by a series of [`macros`][macros] defined in
[`core::fmt`][fmt] some of which are:

- `format!`: write formatted text to [`ByteArray`][bytearray]
- `print!`: same as `format!` but the text is printed to the console
  (stdout).
- `println!`: same as `print!` but a newline is appended.

All parse text in the same fashion. As a plus, Cairo checks formatting
correctness at compile time.

```cairo,editable
{{#include ../../listings/hello/print/src/lib.cairo}}
```

[`core::fmt`][fmt] contains many [`traits`][traits] which govern the display
of text. The base form of two important ones are listed below:

- `fmt::Debug`: Uses the `{:?}` marker. Format text for debugging purposes.
- `fmt::Display`: Uses the `{}` marker. Format text in a more elegant, user
  friendly fashion.

Here, we used `fmt::Display` because the std library provides implementations
for these types. To print text for custom types, more steps are required.

### Activities

- Fix the issue in the above code (see FIXME) so that it runs without
  error.
- Try uncommenting the line that attempts to format the `Structure` struct
  (see TODO)

### See also:

[`std::fmt`][fmt], [`macros`][macros], [`struct`][structs], [`traits`][traits]

[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[macros]: ../macros.md
[bytearray]: ../core/bytearray.md
[structs]: ../custom_types/structs.md
[traits]: https://docs.swmansion.com/scarb/corelib/core-fmt.html#traits
[attribute]: ../attribute.md
