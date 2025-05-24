#[derive(Drop)]
struct ParseError {
    message: ByteArray,
}

// Helper function to parse a single ASCII digit from a ByteArray
fn parse_ascii_digit(value: ByteArray) -> Result<u32, ParseError> {
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

// Define a generic alias for a `Result` with the error type `ParseError`.
type AliasedResult<T> = Result<T, ParseError>;

// Use the above alias to refer to our specific `Result` type.
fn multiply(first_number: ByteArray, second_number: ByteArray) -> AliasedResult<u32> {
    parse_ascii_digit(first_number)
        .and_then(
            |first_number| {
                parse_ascii_digit(second_number).map(|second_number| first_number * second_number)
            },
        )
}

// Here, the alias again allows us to save some space.
fn print(result: AliasedResult<u32>) {
    match result {
        Ok(n) => println!("n is {}", n),
        Err(e) => println!("Error: {}", e.message),
    }
}

fn main() {
    print(multiply("4", "5"));
    print(multiply("t", "2"));
}
