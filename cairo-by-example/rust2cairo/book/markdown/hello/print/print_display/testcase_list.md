# Testcase: List

This is the Cairo adaptation of [Chapter 1.2.2.1 of Rust By Example](https://doc.rust-lang.org/rust-by-example/hello/print/print_display/testcase_list.html):


>  In Cairo, the `?` operator does not work inside loops. Instead, you can `break` with the `Err` value to exit the loop, and use the `?` operator on the returned value.

```cairo
use core::fmt; // Import the `fmt` module.

// Define a structure named `List` containing an `Array`.
#[derive(Drop)]
struct List {
    inner: Array<i32>,
}

impl ListDisplay of fmt::Display<List> {
    fn fmt(self: @List, ref f: fmt::Formatter) -> Result<(), fmt::Error> {
        // Create a span with the array's data.
        let array_span = self.inner.span();

        write!(f, "[")?;

        // Iterate over `i` elements in `array_span`.
        for i in 0..array_span.len() {
            // For every element except the first, add a comma.
            // Use the ? operator to return on errors.
            if i != 0 {
                write!(f, ", ")?;
            }
            write!(f, "{}", *array_span[i])?;
        }

        // Close the opened bracket and return a fmt::Result value.
        write!(f, "]")
    }
}

fn main() {
    let mut arr = ArrayTrait::new();
    arr.append(1);
    arr.append(2);
    arr.append(3);
    let v = List { inner: arr };
    println!("{}", v);
}
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
