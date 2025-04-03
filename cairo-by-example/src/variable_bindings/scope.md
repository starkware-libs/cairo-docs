# Scope and Shadowing

Variable bindings have a scope, and are constrained to live in a _block_. A
block is a collection of statements enclosed by braces `{}`.

```cairo,editable
{{#include ../../listings/variable_bindings/scope/src/lib.cairo}}
```

Also, [variable shadowing][variable-shadow] is allowed.

```cairo,editable
{{#include ../../listings/variable_bindings/scope_2/src/lib.cairo}}
```

[variable-shadow]: https://en.wikipedia.org/wiki/Variable_shadowing
