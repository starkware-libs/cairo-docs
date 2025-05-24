# Literals and operators

Integers `1`, short-strings `'a'`, ByteArrays `"abc"`, booleans `true`
and the unit type `()` can be expressed using literals.

Integers can, alternatively, be expressed using hexadecimal, octal or binary
notation using these prefixes respectively: `0x`, `0o` or `0b`.

Underscores can be inserted in numeric literals to improve readability, e.g.
`1_000` is the same as `1000`.

We need to tell the compiler the type of the literals we use. For now,
we'll use the `u32` suffix to indicate that the literal is an unsigned 32-bit
integer, and the `i32` suffix to indicate that it's a signed 32-bit integer.

```cairo,editable
{{#include ../../listings/literals/src/lib.cairo}}
```

### See also:

- [The Cairo book](https://book.cairo-lang.org/ch02-02-data-types.html)
