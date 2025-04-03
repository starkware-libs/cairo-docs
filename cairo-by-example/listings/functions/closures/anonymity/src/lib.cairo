//ANCHOR: foo
// `F` must be generic.
fn foo<F, +Drop<F>, impl func: core::ops::FnOnce<F, ()>, +Drop<func::Output>>(f: F) {
    f();
}
//ANCHOR_END: foo

//ANCHOR: main
// `F` must implement `Fn` for a closure which takes no
// inputs and returns nothing - exactly what is required
// for `print`.
// `func::Output` must implement `Drop` to ensure the closure's output is properly disposed of
// `F` must implement `Drop` to ensure the closure itself is properly disposed of
fn apply<F, +Drop<F>, impl func: core::ops::Fn<F, ()>, +Drop<func::Output>>(f: F) {
    f();
}

fn main() {
    let x = 7_u8;

    // Capture `x` into an anonymous type and implement
    // `Fn` for it. Store it in `print`.
    let print =  || println!("{}", x);

    // apply(print);
    print();
}
//ANCHOR_END: main


