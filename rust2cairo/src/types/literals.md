# Literals

Numeric literals can be type annotated by adding the type as a suffix. As an example,
to specify that the literal `42` should have the type `i32`, write `42_i32`.

The type of unsuffixed numeric literals will depend on how they are used. If no
constraint exists, the compiler will use `felt252` by default.

```cairo,editable
{{#include ../../listings/types/literals/src/lib.cairo}}
```

[mod]: ../mod.md
[crate]: ../crates.md
