#[derive(Drop)]
struct ParseError {
    message: ByteArray,
}

fn parse_ascii_digit(value: @ByteArray) -> Result<u32, ParseError> {
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

fn double_first(arr: Array<ByteArray>) -> u32 {
    let first = arr[0]; // Generate error 1
    2 * parse_ascii_digit(first).unwrap() // Generate error 2
}

fn main() {
    let numbers = array!["4", "9", "1"];
    let empty = array![];
    let strings = array!["t", "9", "1"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // Error 1: the array is empty

    println!("The first doubled is {}", double_first(strings));
    // Error 2: the element doesn't parse to a number
}
