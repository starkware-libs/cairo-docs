# Returning from loops

One of the uses of a `loop` is to retry an operation until it succeeds. If the
operation returns a value though, you might need to pass it to the rest of the
code: put it after the `break`, and it will be returned by the `loop`
expression.

```cairo,editable
{{#include ../../../listings/flow_control/loop_listing/return_loop_listing/src/lib.cairo}}
```
