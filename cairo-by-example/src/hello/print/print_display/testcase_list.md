# Testcase: List

Implementing `fmt::Display` for a structure where the elements must each be
handled sequentially is tricky. The problem is that each `write!` generates a
`fmt::Result`. Proper handling of this requires dealing with _all_ the
results. Cairo provides the `?` operator for exactly this purpose.

> While the `?` operator is available in the language, it does not work inside loops. You can `break` with the `Err` value to exit the loop, and use the `?` operator on the returned value.

```cairo
{{#include ../../../../listings/hello/print/testcase_list/src/lib.cairo}}
```

### Activity

Try changing the program so that the index of each element in the array is also
printed. The new output should look like this:

```shell
[0: 1, 1: 2, 2: 3]
```

### See also:

[`for`][for], [`ref`][ref], [`Result`][result], [`struct`][struct],
[`?`][q_mark], and [`Array`][array]

[for]: ../../../flow_control/for.md
[result]: ../../../core/result.md
[ref]: ../../../scope/retaining_ownership/snapshots.md
[struct]: ../../../custom_types/structs.md
[q_mark]: ../../../core/result/question_mark.md
[array]: ../../../primitives/array.md
