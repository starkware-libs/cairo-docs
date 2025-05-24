fn modify_array_mut(mut mutable_array: Array<u8>) {
    mutable_array.append(4);
    println!("mutable_array now contains {:?}", mutable_array);
}

fn main() {
    let immutable_array = array![1, 2, 3];

    println!("immutable_array contains {:?}", immutable_array);

    // Mutability error
    // arr.append(4);

    // *Move* the array, changing the ownership (and mutability)
    modify_array_mut(immutable_array);
}
