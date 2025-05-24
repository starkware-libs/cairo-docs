#[derive(Drop)]
struct ParseIntError {
    message: ByteArray,
}

fn char_to_number(c: ByteArray) -> Result<u8, ParseIntError> {
    if c.len() != 1 {
        return Err(ParseIntError { message: "Expected a single character" });
    }
    let byte = c[0];
    Ok(byte)
}

fn main() {
    let result = char_to_number("a");
    match result {
        Ok(number) => println!("Number: 0x{:x}", number),
        Err(error) => println!("Error: {}", error.message),
    }
    let result = char_to_number("ab");
    match result {
        Ok(number) => println!("Number: 0x{:x}", number),
        Err(error) => println!("Error: {}", error.message),
    }
}
