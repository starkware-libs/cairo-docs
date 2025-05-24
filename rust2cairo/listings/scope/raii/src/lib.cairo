fn create_box() {
    // Write an integer to memory and return a pointer to it
    let _box1 = BoxTrait::new(3_u32);
    // `_box1` is dropped here: the associated pointer will no longer be accessible
}

fn main() {
    // Allocate a memory segment for an array and return a pointer to it
    let _box2 = BoxTrait::new(array![1_u8]);

    // A nested scope:
    {
        // Write an integer to memory and return a pointer to it
        let _box3 = BoxTrait::new(4_u32);

        let _pointee_2 = _box2.unbox();
        println!("Pointee 2 is: {:?}", _pointee_2);
        // `_box3` is dropped here: the associated pointer will no longer be accessible
    }
    // `_box2` has been moved to the inner scope when we accessed its inner resources, so it can no
// longer be accessed.
// let pointee_2 = _box2.unbox();
// TODO: uncomment this line and notice the compiler error.
}
