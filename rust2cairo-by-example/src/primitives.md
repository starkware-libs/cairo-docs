# Primitives

Cairo provides access to a variety of `primitives`. A sample includes:

### Scalar Types

- Signed integers: `i8`, `i16`, `i32`, `i64`, `i128`
- Unsigned integers: `u8`, `u16`, `u32`, `u64`, `u128`, `u256`
- Field element: `felt252` (unique to Cairo, represents elements in a finite field)
- `bool` either `true` or `false`
- The unit type `()`, whose only possible value is an empty tuple: `()`

Note that unlike Rust, Cairo doesn't have floating point numbers or char types due to its focus on zero-knowledge proof computations.

### Compound Types

- Fixed-Size Arrays like `[1, 2, 3]`
- Tuples like `(1, true)`

Variables can always be _type annotated_. Numbers may additionally be annotated via a _suffix_. Note that Cairo can also infer types from context.

```cairo,editable
{{#include ../listings/primitives/src/lib.cairo}}
```

### See also:

[the Cairo book][book], [`mut`][mut], [`inference`][inference], and
[`shadowing`][shadowing]

[book]: https://book.cairo-lang.org/
[mut]: variable_bindings/mut.md
[inference]: types/inference.md
[shadowing]: variable_bindings/scope.md
