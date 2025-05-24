# Generics

_Generics_ is the topic of generalizing types and functionalities to broader cases. This is
extremely useful for reducing code duplication in many ways, but can call for rather involved
syntax. Namely, being generic requires taking great care to specify over which types a generic type
is actually considered valid. The simplest and most common use of generics is for type parameters.

A type parameter is specified as generic by the use of angle brackets and upper [camel case][camelcase]: `<Aaa, Bbb, ...>`. "Generic type parameters" are typically represented as `<T>`. In Cairo, "generic" also describes anything that accepts one or more generic type parameters `<T>`. Any type specified as a generic type parameter is generic, and everything else is concrete (non-generic).

For example, defining a _generic function_ named `foo` that takes an argument `T` of any type:

```cairo,ignore
fn foo<T>(arg: T) { ... }
```

Because `T` has been specified as a generic type parameter using `<T>`, it is considered generic when used here as `(arg: T)`. This is the case even if `T` has previously been defined as a `struct`.

This example shows some of the syntax in action:

```cairo,editable
{{#include ../listings/generics/src/lib.cairo}}
```

### See also:

[`structs`][structs]

[structs]: custom_types/structs.md
[camelcase]: https://en.wikipedia.org/wiki/CamelCase
