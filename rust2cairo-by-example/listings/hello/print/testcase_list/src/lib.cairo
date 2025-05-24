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
