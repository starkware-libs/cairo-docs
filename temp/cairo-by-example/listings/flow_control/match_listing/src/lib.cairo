fn main() {
    let number = 13;
    // TODO ^ Try different values for `number`

    println!("Tell me about {}", number);
    match number {
        0 => println!("Zero!"),
        // Match a single value
        1 => println!("One!"),
        // Match several values
        2 | 3 | 4 | 5 => println!("In between 2 and 5"),
        _ => println!("Bigger than 5"),
        // TODO ^ Try commenting out this catch-all arm
    }

    let boolean = true;
    // Match is an expression too
    let binary = match boolean {
        // The arms of a match must cover all the possible values
        false => 0,
        true => 1,
        // TODO ^ Try commenting out one of these arms
    };

    println!("{} -> {}", boolean, binary);
}
