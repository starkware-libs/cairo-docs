# Capturing

Closures are inherently flexible and will do what the functionality requires
to make the closure work without annotation. This allows capturing to
flexibly adapt to the use case, sometimes moving and sometimes borrowing.

Closures can capture variables:

- By snapshot: `@T`
- By value: `T`

They preferentially capture variables by reference and only by value when required.

A restriction of closures is that they cannot capture mutable variables.

```cairo,editable
{{#include ../../../listings/functions/closures/capture/src/lib.cairo}}
```
