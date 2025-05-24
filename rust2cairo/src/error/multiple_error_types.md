# Multiple error types

The previous examples have always been very convenient; `Result`s interact
with other `Result`s and `Option`s interact with other `Option`s.

Sometimes an `Option` needs to interact with a `Result`, or a
`Result<T, Error1>` needs to interact with a `Result<T, Error2>`. In those
cases, we want to manage our different error types in a way that makes them
composable and easy to interact with.

In the following code, two instances of `unwrap` generate different error
types. `array.get()` returns an `Option`, while our `parse_ascii_digit` returns a
`Result<u32, ParseError>`:

```cairo,editable
{{#include ../../listings/error/multiple_error_types/src/lib.cairo}}

```

Over the next sections, we'll see several strategies for handling these kind of problems.
