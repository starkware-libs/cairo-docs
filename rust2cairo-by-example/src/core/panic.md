# `panic!`

The `panic!` macro can be used to generate a panic and start unwinding
its stack. While unwinding, the runtime will take care of freeing all the
resources _owned_ by the thread by calling the destructor of all its objects.

Since we are dealing with programs with only one thread, `panic!` will cause the
program to report the panic message and exit.

```cairo,editable
{{#include ../../listings/core/panic/src/lib.cairo}}
```
