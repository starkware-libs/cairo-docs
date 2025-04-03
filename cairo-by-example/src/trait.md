# Traits

A `trait` is a collection of functions. Unlike in Rust, traits are not defined for a specific implementor type; they can contain methods for different types.

In practice, we often define a trait for a generic type `T`, and then implement that trait for specific types.

In the example below, we define `Animal`, a group of methods over a generic type `T`. The `Animal` trait is then implemented for the `Sheep` data type, allowing the use of methods from `Animal` with a `Sheep`.

The `Sheep` data type also has some methods. In Cairo, type methods are defined in traits, where the `self` type is the type itself. As such, we use the `#[generate_trait]` attribute to automatically generate a trait from the definition of an `impl` containing type methods.

What enables the method syntax is the `self` keyword, which can be used to refer to the implementor type. In that case, any type `T` that implements `Animal` can use the methods defined in `Animal`.

```cairo,editable
{{#include ../listings/trait_listing/src/lib.cairo}}
```
