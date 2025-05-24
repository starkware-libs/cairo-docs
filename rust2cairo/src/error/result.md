# `Result`

[`Result`][result] is a richer version of the [`Option`][option] type that
describes possible _error_ instead of possible _absence_.

That is, `Result<T, E>` could have one of two outcomes:

- `Ok(T)`: An element `T` was found
- `Err(E)`: An error was found with element `E`

By convention, the expected outcome is `Ok` while the unexpected outcome is `Err`.

Like `Option`, `Result` has many methods associated with it. `unwrap()`, for
example, either yields the element `T` or `panic`s. For case handling,
there are many combinators between `Result` and `Option` that overlap.

In working with Cairo, you will likely encounter methods that return the `Result` type.

Let's see what happens when we successfully and unsuccessfully try to convert a character in a ByteArray to a number:

```cairo,editable
{{#include ../../listings/error/result/src/lib.cairo}}
```

In the unsuccessful case, `char_to_number()` returns an error for us to handle.
We can improve the quality of our error message by being more specific
about the return type and considering explicitly handling the error.

[option]: https://docs.swmansion.com/scarb/corelib/core-option-Option.html#option
[result]: https://docs.swmansion.com/scarb/corelib/core-result-Result.html
[`Debug`]: https://docs.swmansion.com/scarb/corelib/core-fmt-Debug.html
[the following section]: result/early_returns.md
