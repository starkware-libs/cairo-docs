# Iterators

The [`Iterator`][iter] trait is used to implement iterators over collections such as arrays.

The trait requires only a method to be defined for the `next` element, which may be manually defined in an `impl` block or automatically defined (as in arrays and ranges).

As a point of convenience for common situations, the `for` construct turns some collections into iterators using the [`.into_iter()`][intoiter] method.

<!-- TODO: fix `take` and `skip` methods -->

```cairo,editable
{{#include ../../listings/trait_listing/iter/src/lib.cairo:all}}
```

[intoiter]: https://docs.swmansion.com/scarb/corelib/core-iter-traits-iterator-IntoIterator.html
[iter]: https://docs.swmansion.com/scarb/corelib/core-iter-traits-iterator-Iterator.html?highlight=trait%20iter#iterator
