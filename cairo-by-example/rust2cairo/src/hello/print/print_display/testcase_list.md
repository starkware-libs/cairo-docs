# Testcase: List

This is the Cairo adaptation of [Chapter 1.2.2.1 of Rust By Example](https://doc.rust-lang.org/rust-by-example/hello/print/print_display/testcase_list.html):


>  In Cairo, the `?` operator does not work inside loops. Instead, you can `break` with the `Err` value to exit the loop, and use the `?` operator on the returned value.

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
