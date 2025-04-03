fn main() {
    // Suffixed literals, their types are known at initialization
    let _x = 1_u8;
    let _y = 2_u32;
    let _z = 3_i32;

    // Unsuffixed literals, their types depend on how they are used
    let _i = 1;
}
