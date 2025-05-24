# Drop and Destruct

The [`Drop`][Drop] trait only has one method: `drop`, which is called automatically when an object
goes out of scope. The main use of the `Drop` trait is to ensure that all dictionaries are
"squashed" when they go out of scope. This "squashing" mechanism ensures that the sequential
accesses to the dictionary are consistent and sound regarding proof generation.

Any type that is not a dictionary can trivially [derive][derive] the `Drop` trait.

The [`Destruct`][Destruct] trait is a more powerful version of the `Drop` trait. It allows for
the developer to specify what should happen when an object goes out of scope.

All types can trivially [derive][derive] the `Destruct` trait, even if they're composed of dictionaries.

The following example adds a print to console to the `drop` function to announce
when it is called.

```cairo,editable
{{#include ../../listings/trait_listing/drop_and_destruct/src/lib.cairo}}
```

[derive]: ./derive.md
[Drop]: https://docs.swmansion.com/scarb/corelib/core-traits-Drop.html
