# Pulling `Result`s out of `Option`s

The most basic way of handling mixed error types is to just embed them in each
other.

```cairo,editable
{{#include ../../../listings/error/multiple_error_types/option_result/src/lib.cairo}}
```
