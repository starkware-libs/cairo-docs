# Display

`fmt::Debug` hardly looks compact and clean, so it is often advantageous to
customize the output appearance. This is done by manually implementing
[`fmt::Display`][fmt], which uses the `{}` print marker. Implementing it
looks like this:

```cairo
{{#include ../../../listings/hello/print/print_display/src/lib.cairo:intro}}
```

`fmt::Display` may be cleaner than `fmt::Debug` but this presents
a problem for the `core` library. How should ambiguous types be displayed?
For example, if the `core` library implemented a single style for all
`Array<T>`, what style should it be? Would it be either of these two?

- `Array<ContractAddress>`: `0x123, 0x456, 0x789` (using hex representation)
- `Array<number>`: `1,2,3` (using decimal representation)

No, because there is no ideal style for all types and the `core` library
doesn't presume to dictate one. `fmt::Display` is not implemented for `Array<T>`
or for any other generic containers. `fmt::Debug` must then be used for these
generic cases.

This is not a problem though because for any new _container_ type which is
_not_ generic, `fmt::Display` can be implemented.

```cairo
{{#include ../../../listings/hello/print/print_display/src/lib.cairo:main}}
```

So, `fmt::Display` has been implemented but `fmt::LowerHex` has not, and therefore
cannot be used. `core::fmt` has many such [`traits`][traits] and each requires
its own implementation. This is detailed further in [`core::fmt`][fmt].

### Activity

After checking the output of the above example, use the `Point2D` struct as a
guide to add a `Complex` struct to the example. When printed in the same
way, the output should be:

```txt
Display: 3 + 7i
Debug: Complex { real: 3, imag: 7 }
```

### See also:

[`derive`][derive], [`core::fmt`][fmt], [`macros`][macros], [`struct`][structs],
[`trait`][traits], and [`use`][use]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[macros]: ../../macros.md
[structs]: ../../custom_types/structs.md
[traits]: ../../trait.md
[use]: ../../mod/use.md
