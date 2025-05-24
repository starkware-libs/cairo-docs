# Traits

Of course `trait`s can also be generic. Here we define one which implements a generic method to drop itself and an input.

```cairo,editable
{{#include ../../listings/generics/gen_trait/src/lib.cairo}}
```

### See also:

[`Drop`][Drop], [`struct`][structs], and [`trait`][traits]

[Drop]: https://book.cairo-lang.org/ch04-01-what-is-ownership.html#no-op-destruction-the-drop-trait
[structs]: ../custom_types/structs.md
[traits]: ../trait.md
