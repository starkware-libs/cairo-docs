# Freezing

When data is bound by the same name immutably, it also _freezes_. _Frozen_ data can't be
modified until the immutable binding goes out of scope:

```cairo,editable
{{#include ../../listings/variable_bindings/freeze/src/lib.cairo}}
```
