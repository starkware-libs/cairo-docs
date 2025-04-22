# Early returns

In the previous example, we explicitly handled the errors using combinators.
Another way to deal with this case analysis is to use a combination of
`match` statements and _early returns_.

That is, we can simply stop executing the function and return the error if
one occurs. For some, this form of code can be easier to both read and
write. Consider this version of the previous example, rewritten using early returns:

```cairo,editable
{{#include ../../../listings/error/result/early_returns/src/lib.cairo}}
```

At this point, we've learned to explicitly handle errors using combinators
and early returns. While we generally want to avoid panicking, explicitly
handling all of our errors is cumbersome.

In the next section, we'll introduce `?` for the cases where we simply
need to `unwrap` without possibly inducing `panic`.
