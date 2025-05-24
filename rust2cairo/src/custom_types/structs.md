# Structures

Structures ("structs") can be created using the `struct` keyword using a classic [C structs][c_struct] syntax.

```cairo,editable
{{#include ../../listings/custom_types/structs/src/lib.cairo}}
```

### Activity

1. Add a function `rect_area` which calculates the area of a `Rectangle` (try
   using nested destructuring).
2. Add a function `square` which takes a `Point` and a `u32` as arguments, and
   returns a `Rectangle` with its top left corner on the point, and a width and
   height corresponding to the `u32`.

### See also

[`Drop`][drop], and [destructuring][destructuring]

[drop]: ../trait/drop.md
[c_struct]: https://en.wikipedia.org/wiki/Struct_(C_programming_language)
[destructuring]: ../flow_control/match/destructuring.md
