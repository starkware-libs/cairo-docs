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

        // Iterate over `v` in `array_span` while enumerating the iteration
        // count in `count`.
        let mut count = 0;
        loop {
            if count >= array_span.len() {
                break Ok(());
            }
            // For every element except the first, add a comma.
            // Use the ? operator to return on errors.
            if count != 0 {
                match write!(f, ", ") {
                    Ok(_) => {},
                    Err(e) => { break Err(e); },
                }
            }
            match write!(f, "{}", *array_span[count]) {
                Ok(_) => {},
                Err(e) => { break Err(e); },
            }
            count += 1;
        }?;

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
