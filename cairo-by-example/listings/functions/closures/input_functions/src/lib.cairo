// Define a function which takes a generic `F` argument
// bounded by `Fn`, and calls it
fn call_me<F, +Drop<F>, impl func: core::ops::Fn<F, ()>, +Drop<func::Output>>(f: F) {
    f();
}

// Define a wrapper function satisfying the `Fn` bound
fn function() {
    println!("I'm a function!");
}

fn main() {
    // Define a closure satisfying the `Fn` bound
    let closure =  || println!("I'm a closure!");

    closure();
    // call_me(closure);
// call_me(function);
// TODO: uncomment the line above and see the compiler error
}
