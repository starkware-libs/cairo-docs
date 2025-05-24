// Globals are declared outside all other scopes.
const LANGUAGE: felt252 = 'Cairo';
const THRESHOLD: u32 = 10;

fn is_big(n: u32) -> bool {
    // Access constant in some function
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Access constant in the main thread
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    let big: ByteArray = "big";
    let small: ByteArray = "small";
    println!("{} is {}", n, if is_big(n) {
        big
    } else {
        small
    });
    // Error! Cannot modify a `const`.
// THRESHOLD = 5;
// FIXME ^ Uncomment this line to see the error
}
