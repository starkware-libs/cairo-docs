# `panic`

The simplest error handling mechanism we will see is `panic`. It prints an
error message, starts unwinding the stack, and exits the program.
Here, we explicitly call `panic` on our error condition:

```cairo,editable
{{#include ../../listings/error/panic_listing/src/lib.cairo}}
```

The first call to `drink` works. The second panics and thus the third is never called.
