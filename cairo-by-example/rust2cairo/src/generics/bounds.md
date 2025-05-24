# Bounds

When working with generics, the type parameters often must use traits as _bounds_ to stipulate what functionality a type implements. For example, the following example uses the trait `Display` to print and so it requires `T` to be bound by `Display`; that is, `T` _must_ implement `Display`.

```cairo,noplayground
{{#include ../../listings/generics/bounds/src/example_1.cairo}}
```

Bounding restricts the generic to types that conform to the bounds. That is:

```cairo,noplayground
{{#include ../../listings/generics/bounds_2/src/lib.cairo}}
```

Another effect of bounding is that generic instances are allowed to access the methods of traits specified in the bounds. For example:

```cairo
{{#include ../../listings/generics/bounds/src/example_2.cairo}}
```

As an additional note, trait bounds in Cairo are specified using the `+` syntax after the generic type parameter. Multiple bounds can be specified by adding additional `+` constraints.

### See also:

[`core::fmt`][fmt], [`struct`s][structs], and [`trait`s][traits]

[fmt]: ../hello/print.md
[methods]: ../fn/methods.md
[structs]: ../custom_types/structs.md
[traits]: ../trait.md
