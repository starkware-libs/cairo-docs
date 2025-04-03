// A concrete type `A`.
#[derive(Copy, Drop)]
struct A {}

// In defining the type `Single`, the first use of `A` is not preceded by `<A>`.
// Therefore, `Single` is a concrete type, and `A` is defined as above.
#[derive(Copy, Drop)]
struct Single {
    value: A,
}
//            ^ Here is `Single`s first use of the type `A`.

// Here, `<T>` precedes the first use of `T`, so `SingleGen` is a generic type.
// Because the type parameter `T` is generic, it could be anything, including
// the concrete type `A` defined at the top.
#[derive(Copy, Drop)]
struct SingleGen<T> {
    value: T,
}

fn main() {
    // `Single` is concrete and explicitly takes `A`.
    let _s = Single { value: A {} };

    // Create a variable `_char` of type `SingleGen<felt252>`
    // and give it the value `SingleGen('a')`.
    // Here, `SingleGen` has a type parameter explicitly specified.
    let _felt: SingleGen<felt252> = SingleGen { value: 'a' };

    // `SingleGen` can also have a type parameter implicitly specified:
    let _t = SingleGen { value: A {} }; // Uses `A` defined at the top.
    let _i32 = SingleGen { value: 6 }; // Uses `felt252`.
    let _felt = SingleGen { value: 'a' }; // Uses `felt252`.
}
