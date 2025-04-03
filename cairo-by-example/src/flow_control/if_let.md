# if let

For some use cases, when matching enums, `match` is awkward. For example:

```cairo, noplayground
{{#include ../../listings/flow_control/if_let/src/lib.cairo:ex_1}}
```

`if let` is cleaner for this use case and in addition allows various
failure options to be specified:

```cairo,editable
{{#include ../../listings/flow_control/if_let/src/lib.cairo:main}}
```

In the same way, `if let` can be used to match any enum value:

```cairo,editable
{{#include ../../listings/flow_control/if_let_2/src/lib.cairo}}
```

Another benefit is that `if let` allows us to match non-parameterized enum variants. This is true even in cases where the enum doesn't implement or derive `PartialEq`. In such cases `if Foo::Bar == a` would fail to compile, because instances of the enum cannot be equated, however `if let` will continue to work.

Would you like a challenge? Fix the following example to use `if let`:

```cairo,editable
{{#include ../../listings/flow_control/if_let_3/src/lib.cairo}}
```

### See also:

[`enum`][enum] and [`Option`][option]

[enum]: ../custom_types/enum.md
[option]: ../core/option.md
