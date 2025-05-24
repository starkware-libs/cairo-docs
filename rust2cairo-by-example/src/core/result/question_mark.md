# `?`

Chaining results using match can get pretty untidy; luckily, the `?` operator
can be used to make things pretty again. `?` is used at the end of an expression
returning a `Result`, and is equivalent to a match expression, where the
`Err(err)` branch expands to an early `return Err(err)`, and the `Ok(ok)`
branch expands to an `ok` expression.

```cairo,editable
{{#include ../../../listings/core/result/question_mark/src/lib.cairo}}
```

Be sure to check the [documentation][docs],
as there are many methods to map/compose `Result`.

[docs]: https://docs.swmansion.com/scarb/corelib/core-result.html
