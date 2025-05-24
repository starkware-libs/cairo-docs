# Introducing `?`

Sometimes we just want the simplicity of `unwrap` without the possibility of
a `panic`. Until now, `unwrap` has forced us to nest deeper and deeper when
what we really wanted was to get the variable _out_. This is exactly the purpose of `?`.

Upon finding an `Err`, there are two valid actions to take:

1. `panic!` which we already decided to try to avoid if possible
2. `return` because an `Err` means it cannot be handled

`?` is _almost_[^†] exactly equivalent to an `unwrap` which `return`s
instead of `panic`king on `Err`s. Let's see how we can simplify the earlier
example that used combinators:

```cairo,editable
{{#include ../../../listings/error/result/enter_question_mark/src/lib.cairo}}
```
