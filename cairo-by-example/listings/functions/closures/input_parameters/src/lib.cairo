// A function which takes a closure as an argument and calls it.
// <F> denotes that F is a "Generic type parameter"
fn apply<F, +Drop<F>, impl func: core::ops::FnOnce<F, ()>, +Drop<func::Output>>(f: F) {
    // ^ TODO: Try changing this to `Fn`.
    f();
}

// A function which takes a closure and returns a `u32`.
fn apply_to_3<F, +Drop<F>, impl func: core::ops::Fn<F, (u32,)>[Output: u32]>(f: F) -> u32 {
    // The closure takes a `u32` and returns a `u32`.
    f(3)
}

fn main() {
    // A non-copy type.
    let greeting: ByteArray = "hello";
    let farewell: ByteArray = "goodbye";

    // // Capture 2 variables: `greeting` by snapshot and
    // // `farewell` by value.
    let diary = 
        || {
            // `greeting` is by snapshot: requires `Fn`.
            println!("I said {}.", greeting);

            // Using farewell by value requires `FnOnce`.
            // Convert farewell to uppercase to demonstrate value capture through `into_iter`
            let mut iter = farewell.into_iter();
            let uppercase: ByteArray = iter.map(|c| if c >= 'a' {
                c - 32
            } else {
                c
            }).collect();
            println!("Then I screamed {}!", uppercase.clone());
        };

    // Call the function which applies the closure.
    // apply(diary);
    diary();

    // `double` satisfies `apply_to_3`'s trait bound
    let double = |x: u32| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}
