# Unpacking options and defaults

There is more than one way to unpack an `Option` and fall back on a default if it is `None`. To choose the one that meets our needs, we need to consider the following:

- do we need eager or lazy evaluation?
- do we need to keep the original empty value intact, or modify it in place?

## `or()` is chainable, evaluates eagerly, keeps empty value intact

`or()`is chainable and eagerly evaluates its argument, as is shown in the following example. Note that because `or`'s arguments are evaluated eagerly, the variable passed to `or` is moved.

```cairo,editable
{{#include ../../../listings/error/option_unwrap/defaults_or/src/lib.cairo}}
```

## `or_else()` is chainable, evaluates lazily, keeps empty value intact

Another alternative is to use `or_else`, which is also chainable, and evaluates lazily, as is shown in the following example:

```cairo,editable
{{#include ../../../listings/error/option_unwrap/defaults_or_else/src/lib.cairo}}
```

### See also:

[`closures`][closures], [`moved variables`][moved], [`or`][or], [`or_else`][or_else]

[closures]: https://book.cairo-lang.org/ch11-01-closures.html
[moved]: https://book.cairo-lang.org/ch04-01-what-is-ownership.html#ownership-using-a-linear-type-system
[or]: https://docs.swmansion.com/scarb/corelib/core-option-OptionTrait.html#or
[or_else]: https://docs.swmansion.com/scarb/corelib/core-option-OptionTrait.html#or_else
