# Defining an error type

Sometimes it simplifies the code to mask all of the different errors with a
single type of error. We'll show this with a custom error.

Cairo allows us to define our own error types. In general, a "good" error type:

- Represents different errors with the same type
- Presents nice error messages to the user
- Is easy to compare with other types
  - Good: `Result::Err(EmptyArray)`
  - Bad: `Result::Err("Please use an array with at least one element")`
- Can hold information about the error
  - Good: `Result::Err(BadChar(c, position))`
  - Bad: `Result::Err("+ cannot be used here")`
- Composes well with other errors

```cairo,editable
{{#include ../../../listings/error/multiple_error_types/define_error_type/src/lib.cairo}}
```
