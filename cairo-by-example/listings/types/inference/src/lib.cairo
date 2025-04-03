fn main() {
    // Because of the annotation, the compiler knows that `elem` has type u8.
    let elem = 5_u8;

    // Create an empty array.
    let mut array = array![];
    // At this point the compiler doesn't know the exact type of `array`, it
    // just knows that it's an array of something (`Array<_>`).

    // Insert `elem` in the vector.
    array.append(elem);
    // Aha! Now the compiler knows that `array` is an array of `u8`s (`Array<u8>`)
    // TODO ^ Try commenting out the `array.append(elem)` line

    println!("{:?}", array);
}
