# The Problem

A `trait` that is generic over its container type has type specification requirements - users of the `trait` _must_ specify all of its generic types.

In the example below, the `Contains` `trait` allows the use of the generic types `A` and `B`, and can be implemented for any container `C`. The trait is then implemented for the concrete `Container` type, specifying `i32` for `A` and `B` so that it can be used with `fn difference()`.

Because `Contains` is generic, we are forced to explicitly state _all_ of the generic types for `fn difference()`. In practice, we want a way to express that `A` and `B` are determined by the _input_ `C`. As you will see in the next section, associated types provide exactly that capability.

```cairo,editable
{{#include ../../../listings/generics/assoc_items/the_problem/src/lib.cairo}}
```

### See also:

[`struct`s][structs], and [`trait`s][traits]

[structs]: ../../custom_types/structs.md
[traits]: ../../trait.md
