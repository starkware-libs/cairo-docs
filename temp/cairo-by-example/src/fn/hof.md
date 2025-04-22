# Higher Order Functions

Cairo provides Higher Order Functions (HOF). These are functions that
take one or more functions and/or produce a more useful function. HOFs
and iterators give Cairo its functional flavor.

```cairo,editable
{{#include ../../listings/functions/hof/src/lib.cairo}}
```

[Option][option]
and
[Iterator][iter]
implement their fair share of HOFs.

[option]: https://docs.swmansion.com/scarb/corelib/core-option-Option.html
[iter]: https://docs.swmansion.com/scarb/corelib/core-iter-traits-iterator-Iterator.html
