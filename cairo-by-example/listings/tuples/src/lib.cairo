// Tuples can be used as function arguments and as return values.
fn reverse(pair: (felt252, bool)) -> (bool, felt252) {
    // `let` can be used to bind the members of a tuple to variables.
    let (int_param, bool_param) = pair;
    (bool_param, int_param)
}

fn main() {
    // A tuple with a bunch of different types
    let tuple: (u8, ByteArray, i8, bool) = (1, "hello", -1, true);
    // Tuples can be destructured to create bindings.
    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    // Tuples can be tuples members.
    let tuple_of_tuples: ((u8, u16, u32), (u64, i8), i16) = ((1, 2, 3), (4, -1), -2);

    // Tuple are printable.
    println!("tuple_of_tuples: {:?}", tuple_of_tuples);

    // But long Tuples (more than 17 elements) cannot be created.
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17);
    // println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error

    // Creating and using a pair tuple.
    let pair = (1, true);
    println!("Pair is {:?}", pair);

    // To create one element tuples, the comma is required to tell them apart
    // from a literal surrounded by parentheses.
    println!("One element tuple: {:?}", (5_u32,));
    println!("Just an integer: {:?}", (5_u32));

    // One-element tuple declaration.
    let one_element_tuple: (u32,) = (5,);
    let (element,) = one_element_tuple;
    println!("element: {}", element);
}
