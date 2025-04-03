# Combinators: `map`

`match` is a valid method for handling `Option`s. However, you may
eventually find heavy usage tedious, especially with operations only valid
with an input. In these cases, combinators can be used to
manage control flow in a modular fashion.

`Option` has a built in method called `map()`, a combinator for the simple
mapping of `Some -> Some` and `None -> None`. Multiple `map()` calls can be
chained together for even more flexibility.

In the following example, `process()` replaces all functions previous
to it while staying compact.

```cairo,editable
{{#include ../../../listings/error/option_unwrap/map/src/lib.cairo}}
```

### See also:

[closures][closures], [`Option`][option], [`Option::map()`][map]

[closures]: ../../fn/closures.md
[option]: https://docs.swmansion.com/scarb/corelib/core-option-Option.html
[map]: https://docs.swmansion.com/scarb/corelib/core-option-OptionTrait.html#map
