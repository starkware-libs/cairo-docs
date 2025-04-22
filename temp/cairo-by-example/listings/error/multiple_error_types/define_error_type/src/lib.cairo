type Result<T> = core::result::Result<T, DoubleError>;

// Define our error types. These may be customized for our error handling cases.
// Now we will be able to write our own errors, defer to an underlying error
// implementation, or do something in between.
#[derive(Drop, Debug)]
enum DoubleError {
    EmptyArray,
    Parse,
}

impl DoubleErrorImpl of core::fmt::Display<DoubleError> {
    fn fmt(
        self: @DoubleError, ref f: core::fmt::Formatter,
    ) -> core::result::Result<(), core::fmt::Error> {
        match self {
            DoubleError::EmptyArray => write!(f, "please use an array with at least one element"),
            DoubleError::Parse => write!(f, "invalid digit to double"),
        }
    }
}

#[derive(Drop)]
struct ParseError {
    message: ByteArray,
}

fn parse_ascii_digit(value: @ByteArray) -> core::result::Result<u32, ParseError> {
    if value.len() != 1 {
        Err(ParseError { message: "Expected a single character" })
    } else {
        let byte = value[0];
        if byte >= '0' && byte <= '9' {
            Ok((byte - '0').into())
        } else {
            Err(ParseError { message: "Character is not a digit" })
        }
    }
}

fn double_first(arr: Array<ByteArray>) -> Result<u32> {
    arr
        .get(0)
        // Change the error to our new type.
        .ok_or(DoubleError::EmptyArray)
        .and_then(
            |s| {
                parse_ascii_digit(s.unbox()) // Update to the new error type here also.
                    .map_err(|_err| DoubleError::Parse)
                    .map(|i| 2 * i)
            },
        )
}

fn print(result: Result<u32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = array!["4", "9", "1"];
    let empty = array![];
    let strings = array!["t", "9", "1"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
