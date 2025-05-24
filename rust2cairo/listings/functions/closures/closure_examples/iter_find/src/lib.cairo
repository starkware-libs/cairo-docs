fn main() {
    let array = array![1_u8, 2, 3];
    let span = array![4_u8, 5, 6].span();

    // `into_iter()` for arrays yields elements by value
    let mut iter = array.into_iter();
    // `into_iter()` for spans yields elements by snapshot
    let mut into_iter = span.into_iter();

    // `into_iter()` for arrays yields `@T`, and we want to reference one of
    // its items, so we have to destructure `@T` to `T`
    println!("Find 2 in array: {:?}", iter.find(|x| *x == 2));
    // `into_iter()` for spans yields `@T`, and we want to reference one of
    // its items, so we have to compare with `@@T`
    println!("Find 2 in span: {:?}", into_iter.find(|x| x == @@2));
}
