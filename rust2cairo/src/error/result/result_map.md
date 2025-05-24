# `map` for `Result`

Panicking in the previous example's `multiply` does not make for robust code.
Generally, we want to return the error to the caller so it can decide what is
the right way to respond to errors.

We first need to know what kind of error type we are dealing with. To determine
the `Err` type, we look to our `parse_ascii_digit` function, which returns a `ParseError` type.

In the example below, the straightforward `match` statement leads to code
that is overall more cumbersome.

```cairo,editable
{{#include ../../../listings/error/result/result_map/src/lib.cairo}}
```

Luckily, `Option`'s `map`, `and_then`, and many other combinators are also
implemented for `Result`. [`Result`][result] contains a complete listing.

```cairo,editable
{{#include ../../../listings/error/result/result_map_2/src/lib.cairo}}
```

[result]: https://docs.swmansion.com/scarb/corelib/core-result-Result.html
