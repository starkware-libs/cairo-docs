# Struct visibility

Structs have an extra level of visibility with their fields. The visibility
defaults to private, and can be overridden with the `pub` modifier. This
visibility only matters when a struct is accessed from outside the module
where it is defined, and has the goal of hiding information (encapsulation).

```cairo,editable
{{#include ../../listings/mod/struct_visibility/src/lib.cairo}}
```

### See also:

[generics][generics] and [methods][methods]

[generics]: ../generics.md
[methods]: ../fn/methods.md
