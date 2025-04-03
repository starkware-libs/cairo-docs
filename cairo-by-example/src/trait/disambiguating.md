# Disambiguating overlapping traits

A type can implement many different traits. What if two traits both require the same name for a function? For example, many traits might have a method named `get()`. They might even have different return types!

Good news: because each trait implementation gets its own `impl` block with a unique name, it's clear which trait's `get` method you're implementing.

What about when it comes time to _call_ those methods? To disambiguate between them, we have to use Fully Qualified Syntax.

```cairo,editable
{{#include ../../listings/trait_listing/disambiguating/src/lib.cairo}}
```

### See also:

[The Cairo Book chapter on Traits][cairo_traits]

[cairo_traits]: https://book.cairo-lang.org/ch08-02-traits-in-cairo.html
