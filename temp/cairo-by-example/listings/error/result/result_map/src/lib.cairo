#[derive(Drop)]
struct ParseError {
    message: ByteArray,
}

// Helper function to parse a single ASCII digit from a ByteArray
fn parse_ascii_digit(value: ByteArray) -> Result<u32, ParseError> {
    if value.len() != 1 {
        Result::Err(ParseError { message: "Expected a single character" })
    } else {
        let byte = value[0];
        if byte >= '0' && byte <= '9' {
            Result::Ok((byte - '0').into())
        } else {
            Result::Err(ParseError { message: "Character is not a digit" })
        }
    }
}

// With the return type rewritten, we use pattern matching without `unwrap()`.
fn multiply(first_number: ByteArray, second_number: ByteArray) -> Result<u32, ParseError> {
    match parse_ascii_digit(first_number) {
        Result::Ok(first_number) => {
            match parse_ascii_digit(second_number) {
                Result::Ok(second_number) => { Result::Ok(first_number * second_number) },
                Result::Err(e) => Result::Err(e),
            }
        },
        Result::Err(e) => Result::Err(e),
    }
}

fn print(result: Result<u32, ParseError>) {
    match result {
        Result::Ok(n) => println!("n is {}", n),
        Result::Err(e) => println!("Error: {}", e.message),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("4", "5");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
