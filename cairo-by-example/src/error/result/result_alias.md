# aliases for `Result`

How about when we want to reuse a specific `Result` type many times?
Cairo allows us to create type aliases. Conveniently,
we can define one for the specific `Result` in question.

At a module level, creating aliases can be particularly helpful. Errors
found in a specific module often have the same `Err` type, so a single alias
can succinctly define _all_ associated `Results`.

Here's a quick example to show off the syntax:

```cairo,editable
{{#include ../../../listings/error/result/result_alias/src/lib.cairo}}
```

### See also:

[typealias]: ../../types/alias.md
