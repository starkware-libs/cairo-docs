// Define a function `printer` that takes a generic type `T` which
// must implement trait `Display`.
fn printer<T, +core::fmt::Display<T>, +Drop<T>>(t: T) {
    println!("{}", t);
}
