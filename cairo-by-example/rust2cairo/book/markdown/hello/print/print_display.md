# Display

This is the Cairo adaptation of [Rust By Example's _Display_ chapter](https://doc.rust-lang.org/rust-by-example/hello.html):

```cairo, editable
use core::fmt; // Import `fmt`

// A structure holding two numbers. `Debug` will be derived so the results can
// be contrasted with `Display`.
#[derive(Debug, Drop)]
struct MinMax {
    min: i64,
    max: i64,
}

// Implement `Display` for `MinMax`.
impl MinMaxDisplay of fmt::Display<MinMax> {
    fn fmt(self: @MinMax, ref f: fmt::Formatter) -> Result<(), fmt::Error> {
        // Use `self.number` to refer to each positional data point.
        write!(f, "({}, {})", *self.min, *self.max)
    }
}

// Define a structure where the fields are nameable for comparison.
#[derive(Debug, Drop)]
struct Point2D {
    x: i64,
    y: i64,
}

// Similarly, implement `Display` for `Point2D`.
impl Point2DDisplay of fmt::Display<Point2D> {
    fn fmt(self: @Point2D, ref f: fmt::Formatter) -> Result<(), fmt::Error> {
        // Customize so only `x` and `y` are denoted.
        write!(f, "x: {}, y: {}", *self.x, *self.y)
    }
}

fn main() {
    let minmax = MinMax { min: 0, max: 14 };

    println!("Compare structures:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range = MinMax { min: -300, max: 300 };
    let small_range = MinMax { min: -3, max: 3 };

    println!("The big range is {} and the small is {}", big_range, small_range);

    let point = Point2D { x: 3, y: 7 };

    println!("Compare points:");
    println!("Display: {}", point);
    // Error. Both `Debug` and `Display` were implemented, but `{:x}`
// requires `fmt::LowerHex` to be implemented. This will not work.
// println!("What does Point2D look like in binary: {:x}?", point);
}
```

### Activity

After checking the output of the above example, use the `Point2D` struct as a guide to add a `Complex` struct to the example. When printed in the same way, the output should be:

```txt
Display: 3 + 7i
Debug: Complex { real: 3, imag: 7 }
```

### See also:

[`derive`][derive], [`core::fmt`][fmt], [`macros`][macros], [`struct`][structs],
[`trait`][traits], and [`use`][use]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
[structs]: ../../custom_types/structs.md
[traits]: ../../trait.md
[use]: ../../mod/use.md
