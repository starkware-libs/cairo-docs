# Clone

When dealing with values in Cairo, the default behavior is to transfer ownership during assignments or function calls. However, sometimes we need to make a clone of the value as well.

The `Clone` trait helps us do exactly this. Most commonly, we can use the `.clone()` method defined by the `Clone` trait.

```cairo,editable
{{#include ../../listings/trait_listing/clone/src/lib.cairo}}

```

[clone]: https://docs.swmansion.com/scarb/corelib/core-clone-Clone.html
