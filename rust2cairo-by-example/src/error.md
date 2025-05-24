# Error handling

Error handling is the process of handling the possibility of failure. For
example, failing to parse a number from a string and then continuing to use that _bad_ input
would clearly be problematic. Noticing and explicitly managing those errors
saves the rest of the program from various pitfalls.

There are various ways to deal with errors in Cairo, which are described in the
following subchapters. They all have more or less subtle differences and different
use cases. As a rule of thumb:

An explicit `panic` is mainly useful for tests and dealing with unrecoverable errors, or to assert
that a condition must never happens. For prototyping it can be useful, for example when dealing with
functions that haven't been implemented yet. In tests `panic` is a reasonable way to explicitly
fail.

The `Option` type is for when a value is optional or when the lack of a value is
not an error condition. For attempting to convert a value `V` to a `NonZero<V>` - which would fail if said value is zero. When dealing with `Option`s, `unwrap` is fine for prototyping and cases
where it's absolutely certain that there is guaranteed to be a value. However `expect`
is more useful since it lets you specify an error message in case something goes
wrong anyway.

When there is a chance that things do go wrong and the caller has to deal with the
problem, use `Result`. You can `unwrap` and `expect` them as well, but a proper error handling strategy is preferred.

For a more rigorous discussion of error handling, refer to the error
handling section in the [official book][book].

[book]: https://book.cairo-lang.org/ch09-00-error-handling.html
