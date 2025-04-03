mod intro {
    //ANCHOR:intro
    // Import (via `use`) the `fmt` module to make it available.
    use core::fmt;

    // Define a structure for which `fmt::Display` will be implemented. This is
    // a tuple struct named `Structure` that contains an integer.
    #[derive(Drop)]
    struct Structure {
        value: u32,
    }

    // To use the `{}` marker, the trait `fmt::Display` must be implemented
    // manually for the type.
    impl StructureDisplay of fmt::Display<Structure> {
        // This trait requires `fmt` with this exact signature.
        fn fmt(self: @Structure, ref f: fmt::Formatter) -> Result<(), fmt::Error> {
            // Write strictly the first element into the supplied output
            // stream: `f`. Returns `fmt::Result` which indicates whether the
            // operation succeeded or failed. Note that `write!` uses syntax which
            // is very similar to `println!`.
            write!(f, "{}", *self.value)
        }
    }
    //ANCHOR_END:intro
}

//ANCHOR:main
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
//ANCHOR_END:main


