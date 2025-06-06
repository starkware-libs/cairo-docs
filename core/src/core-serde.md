# serde

Serialization and deserialization of data structures.
This module provides traits and implementations for converting Cairo types into a sequence of
`felt252` values (serialization) and back (deserialization).
When passing values between Cairo and an external environment, serialization and deserialization
are necessary to convert Cairo's data types into a sequence of `felt252` values, as `felt252` is
the fundamental type of the language.
# The `Serde` Trait

All types that need to be serialized must implement the `Serde` trait. This includes both simple
types that serialize to a single `felt252` and compound types (like `u256`) that require
multiple `felt252` values.

Fully qualified path: [core](./core.md)::[serde](./core-serde.md)


[Modules](./core-serde-modules.md)
 ---
| | |
|:---|:---|
| [into_felt252_based](./core-serde-into_felt252_based.md) | [...](./core-serde-into_felt252_based.md) |

[Traits](./core-serde-traits.md)
 ---
| | |
|:---|:---|
| [Serde](./core-serde-Serde.md) | A trait that allows for serializing and deserializing values of any type. The `Serde<T>`  trait defines two core operations:[...](./core-serde-Serde.md) |
