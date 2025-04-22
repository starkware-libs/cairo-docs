fn main() {
    let outer_var = 42_u32;

    // A regular function can't be defined in the body of another function.
    // fn function(i: u32) -> u32 { i + outer_var };
    // TODO: uncomment the line above and see the compiler error.

    // Closures are anonymous, here we are binding them to references.
    // Annotation is identical to function annotation but is optional
    // as are the `{}` wrapping the body. These nameless functions
    // are assigned to appropriately named variables.
    let closure_inferred = |i| i + outer_var;

    // Call the closures
    println!("closure_inferred: {}", closure_inferred(1_u32));
    // Once closure's type has been inferred, it cannot be inferred again with another type.
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42_u64));
    // TODO: uncomment the line above and see the compiler error

    // A closure taking no arguments which returns a `u32`.
    // The return type is inferred.
    let one =  || 1_u32;
    println!("closure returning one: {}", one());
}
