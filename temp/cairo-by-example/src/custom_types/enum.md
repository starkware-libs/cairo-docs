# Enums

The `enum` keyword allows the creation of a type which may be one of a few
different variants. Any variant which is valid as a `struct` is also valid in
an `enum`.

```cairo,editable
{{#include ../../listings/custom_types/enum_1/src/lib.cairo}}
```

## Type aliases

If you use a type alias, you can refer to each enum variant via its alias.
This might be useful if the enum's name is too long or too generic, and you
want to rename it.

```cairo,editable
{{#include ../../listings/custom_types/enum_2/src/lib.cairo:one}}
```

### See also:

[`match`][match], [`fn`][fn], and [`ByteArray`][str]

[match]: ../flow_control/match.md
[fn]: ../fn.md
[str]: ../core/bytearray.md
