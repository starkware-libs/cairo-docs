# `unused_imports`

The compiler provides a `unused_imports`
[_lint_][lint] that will warn
about unused imports. An _attribute_ can be used to disable the lint.

```cairo,editable
{{#include ../../listings/attribute/unused/src/lib.cairo}}
```

Note that in real programs, you should eliminate dead code. In these examples
we'll allow dead code in some places because of the interactive nature of the
examples.

[lint]: https://en.wikipedia.org/wiki/Lint_%28software%29
