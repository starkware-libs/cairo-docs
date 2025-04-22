# Associated types

The use of "Associated types" improves the overall readability of code by moving inner types locally into a trait as _output_ types. Syntax for the `trait` definition is as follows:

```cairo
{{#include ../../../listings/generics/assoc_items/types/src/example_1.cairo}}
```

Note that functions that use the `trait` `Contains` are no longer required to express `A` or `B` at all:

```cairo
// Without using associated types
fn difference<A, B, C, +Contains<C, A, B>>(container: @C) -> i32 { ... }

// Using associated types
fn difference<T, +Contains<T>>(container: @T) -> i32 { ... }

```

Let's rewrite the example using associated types:

```cairo, editable
{{#include ../../../listings/generics/assoc_items/types/src/example_2.cairo}}
```
