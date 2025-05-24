# Unpacking options with `?`

You can unpack `Option`s by using `match` statements, but it's often easier to
use the `?` operator. If `x` is an `Option`, then evaluating `x?` will return
the underlying value if `x` is `Some`, otherwise it will terminate whatever
function is being executed and return `None`.

```cairo, noplayground
{{#include ../../../listings/error/option_unwrap/question_mark/src/lib.cairo:intro}}
```

You can chain many `?`s together to make your code much more readable.

```cairo,editable
{{#include ../../../listings/error/option_unwrap/question_mark/src/lib.cairo:main}}
```
