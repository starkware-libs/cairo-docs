fn main() {
    let color: ByteArray = "green";

    // A closure to print `color` which immediately takes by snapshot (`@`) `color` and
    // stores the snapshot and closure in the `print` variable. It will remain
    // borrowed until `print` is used the last time.
    //
    // `println!` only requires arguments by snapshot so it doesn't
    // impose anything more restrictive.
    let print =  || println!("`color`: {}", color);

    // Call the closure using the borrow.
    print();

    // `into_iter` requires `T` so this must take by value. A copy type
    // would copy into the closure leaving the original untouched.
    // A non-copy must move the value into the closure.
    let consume = 
        || {
            println!("`color`: {}", color);
            let mut iter = color.into_iter();
            println!("`byte_0`: 0x{:x}", iter.next().unwrap());
        };

    // `consume` consumes the variable so this can only be called once.
    consume();
    // consume();
// ^ TODO: Try uncommenting this line.
}
