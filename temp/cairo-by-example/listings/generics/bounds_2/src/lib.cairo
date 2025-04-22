//TAG: does_not_compile
#[derive(Drop)]
struct S<T, +core::fmt::Display<T>> {
    value: T,
}

// Error! `Array<T>` does not implement `Display`. This
// specialization will fail.
fn foo() {
    let _s = S { value: array![1] };
}
