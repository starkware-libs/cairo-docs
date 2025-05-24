# match

Cairo provides pattern matching via the `match` keyword, which can be used like
a C `switch`. The first matching arm is evaluated and all possible values must be
covered.

> A limitation of the `match` statement applied to integers is that the values in the arms must be sequential, starting from 0.

```cairo,editable
{{#include ../../listings/flow_control/match_listing/src/lib.cairo}}
```
