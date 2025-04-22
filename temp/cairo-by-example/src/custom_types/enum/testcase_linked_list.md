# Testcase: linked-list

A common way to implement a linked-list is via `enums`. In Cairo, we'll implement a simple linked list that stores its nodes directly in the enum:

```cairo,editable
{{#include ../../../listings/custom_types/enum/linked_list/src/lib.cairo}}
```

### See also:

[traits][traits] and [methods][methods]

[traits]: ../../trait.md
[methods]: ../../fn/methods.md
[box]: ../../core/box.md
