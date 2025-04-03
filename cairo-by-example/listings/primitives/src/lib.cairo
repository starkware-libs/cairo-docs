fn main() {
    // Variables can be type annotated.
    let logical: bool = true;

    // Integer annotations
    let an_integer: u32 = 5_u32; // Regular annotation
    let another_integer = 5_u32; // Suffix annotation

    // felt252 is Cairo's native field element type
    let a_felt = 3; // Default to felt252
    let explicit_felt: felt252 = 3;

    // A type can also be inferred from context
    let mut inferred_type = 12_u64; // Type u64 is inferred
    inferred_type = 4294967296_u64;

    // A mutable variable's value can be changed
    let mut mutable = 12_u32; // Mutable `u32`
    mutable = 21_u32;

    // Error! The type of a variable can't be changed
    // mutable = true;

    // Variables can be overwritten with shadowing
    let mutable = true;

    // Compound types - Array and Tuple //

    // Array signature consists of Type T and length as [T; length]
    let my_array: [u32; 5] = [1_u32, 2_u32, 3_u32, 4_u32, 5_u32];

    // Tuple is a collection of values of different types
    // and is constructed using parentheses ()
    let my_tuple: (u32, u8, bool, felt252) = (5_u32, 1_u8, true, 123);
}
