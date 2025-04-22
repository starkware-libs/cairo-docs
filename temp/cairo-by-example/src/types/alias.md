# Aliasing

The `type` statement can be used to give a new name to an existing type. Types
must have `UpperCamelCase` names, or the compiler will raise a warning. The
exception to this rule are the primitive types: `usize`, `f32`, etc.

```cairo,editable
{{#include ../../listings/types/alias/src/lib.cairo}}
```

The main use of aliases is to reduce boilerplate; for example the `SyscallResult<T>` type
is an alias for the `Result<(), Error>` type.

### See also:

[Attributes](../attribute.md)
