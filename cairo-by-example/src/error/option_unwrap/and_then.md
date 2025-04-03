# Combinators: `and_then`

`map()` was described as a chainable way to simplify `match` statements.
However, using `map()` on a function that returns an `Option<T>` results
in the nested `Option<Option<T>>`. Chaining multiple calls together can
then become confusing. That's where another combinator called `and_then()`,
known in some languages as flatmap, comes in.

`and_then()` calls its function input with the wrapped value and returns the result. If the `Option` is `None`, then it returns `None` instead.

In the following example, `cookable_v3()` results in an `Option<Food>`.
Using `map()` instead of `and_then()` would have given an
`Option<Option<Food>>`, which is an invalid type for `eat()`.

```cairo,editable
{{#include ../../../listings/error/option_unwrap/and_then/src/lib.cairo:main}}
```

### See also:

[closures][closures], [`Option`][option], [`Option::and_then()`][and_then]

[closures]: ../../fn/closures.md
[option]: https://docs.swmansion.com/scarb/corelib/core-option-Option.html#option
[and_then]: https://docs.swmansion.com/scarb/corelib/core-option-OptionTrait.html#and_then
