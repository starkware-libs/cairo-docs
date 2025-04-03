#[derive(Drop)]
struct A {} // Concrete type `A`.
#[derive(Drop)]
struct S { // Concrete type `S`.
    value: A,
}
#[derive(Drop)]
struct SGen<T> { // Generic type `SGen`.
    value: T,
}

// The following functions all take ownership of the variable passed into
// them and immediately go out of scope, freeing the variable.

// Define a function `reg_fn` that takes an argument `_s` of type `S`.
// This has no `<T>` so this is not a generic function.
fn reg_fn(_s: S) {}

// Define a function `gen_spec_t` that takes an argument `_s` of type `SGen<T>`.
// It has been explicitly given the type parameter `A`, but because `A` has not
// been specified as a generic type parameter for `gen_spec_t`, it is not generic.
fn gen_spec_t(_s: SGen<A>) {}

// Define a function `gen_spec_i32` that takes an argument `_s` of type `SGen<i32>`.
// It has been explicitly given the type parameter `i32`, which is a specific type.
// Because `i32` is not a generic type, this function is also not generic.
fn gen_spec_i32(_s: SGen<i32>) {}

// Define a function `generic` that takes an argument `_s` of type `SGen<T>`.
// Because `SGen<T>` is preceded by `<T>`, this function is generic over `T`.
// We need T to implement the Drop trait to go out of scope.
fn generic<T, impl TDrop: Drop<T>>(_s: SGen<T>) {}

fn main() {
    // Using the non-generic functions
    reg_fn(S { value: A {} }); // Concrete type.
    gen_spec_t(SGen { value: A {} }); // Implicitly specified type parameter `A`.
    gen_spec_i32(SGen { value: 6 }); // Implicitly specified type parameter `i32`.

    // Explicitly specified type parameter `felt252` to `generic()`.
    generic::<felt252>(SGen { value: 'a' });

    // Implicitly specified type parameter `felt252` to `generic()`.
    generic(SGen { value: 'c' });
}
