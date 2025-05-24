// This function takes ownership of the array, because `Array<u128>` does not implement `Copy`.
fn pass_by_value_move(arr: Array<u128>) {
    println!("dropped an array of length {}", arr.len());
    // `arr` is dropped when it goes out of scope
}

// This function does not take ownership of the value,
// because `u128` implements `Copy`.
fn pass_by_value_copy(c: u128) {
    println!("dropped a value that contains {}", c);
    // `c` is dropped when it goes out of scope
}

fn main() {
    // Simple integer value
    let x = 5_u128;

    // Pass `x` by value to a function: because `u128` implements `Copy`, ownership is not moved.
    pass_by_value_copy(x);
    println!("x is {}", x);

    // Create an array (arrays don't implement Copy)
    let mut arr = array![5];

    println!("arr contains: {:?}", arr);

    // *Move* `arr` into `pass_by_value_move`
    pass_by_value_move(arr);
    // Error! `arr` can no longer be used since it was moved
// println!("arr contains: {:?}", arr));
// TODO ^ Try uncommenting this line

}
