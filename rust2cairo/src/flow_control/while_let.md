# while let

Similar to `if let`, `while let` can make awkward `match` sequences
more tolerable. Consider the following sequence that increments `i`:

```cairo
{{#include ../../listings/flow_control/while_let/src/lib.cairo}}
```

Using `while let` makes this sequence much nicer:

```cairo,editable
{{#include ../../listings/flow_control/while_let_2/src/lib.cairo}}
```

### See also:

[`enum`][enum] and [`Option`][option]

[enum]: ../custom_types/enum.md
[option]: ../core/option.md
