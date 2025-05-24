use core::fmt::{Debug, Display};

// T must implement both Debug and Display
fn compare_prints<T, +Debug<T>, +Display<T>>(t: @T) {
    println!("Debug: `{:?}`", t);
    println!("Display: `{}`", t);
}

// T and U must both implement Debug
fn compare_types<T, U, +Debug<T>, +Debug<U>>(t: @T, u: @U) {
    println!("t: `{:?}`", t);
    println!("u: `{:?}`", u);
}

fn main() {
    let string: ByteArray = "words";
    let array = array![1, 2, 3];
    let vec = array![1, 2, 3];

    compare_prints(@string);
    // compare_prints(@array);
    // TODO ^ Try uncommenting this line.
    // Error: Array does not implement Display

    compare_types(@array, @vec);
}
