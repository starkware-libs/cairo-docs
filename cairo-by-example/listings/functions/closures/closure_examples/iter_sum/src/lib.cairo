//TAG: does_not_compile
fn main() {
    let array = array![1_u8, 2, 3];
    let span = array![4_u8, 5, 6].span();

    // `into_iter()` for arrays yields elements by value
    println!("sum of array: {}", array.into_iter().sum());
    // `into_iter()` for spans yields elements by snapshot
    println!("sum of span: {}", span.into_iter().sum());

    // `into_iter` takes ownership of the value passed.
    // Because `Span` implements copy, it can be used again.
    println!("span length: {}", span.len());
    println!("First element of span: {}", span[0]);
    // Because `Array` doesn't implement copy, it can't be used again.
// println!("array length: {}", array.len()); // This would not compile
// println!("First element of array: {}", array[0]); // This would not compile
// TODO: uncomment the two lines above and see compiler errors.
}
