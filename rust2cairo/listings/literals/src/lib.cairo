fn main() {
    // Integer addition
    println!("1 + 2 = {}", 1_u32 + 2);

    // Integer subtraction
    println!("1 - 2 = {}", 1_i32 - 2);
    // TODO ^ Try changing `1i32` to `1u32` to see why the type is important

    // Short-circuiting boolean logic
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Bitwise operations
    println!("0011 AND 0101 is {}", 0b0011_u32 & 0b0101);
    println!("0011 OR 0101 is {}", 0b0011_u32 | 0b0101);
    println!("0011 XOR 0101 is {}", 0b0011_u32 ^ 0b0101);

    // Use underscores to improve readability!
    println!("One million is written as {}", 1_000_000_u32);

    // A short-string is the ASCII encoding of the characters.
    println!("Short string `a`: {}", 'a');
}
