// This structure cannot be printed with `fmt::Display` or
// with `fmt::Debug` by default.
#[derive(Drop)]
struct UnPrintable {
    value: felt252,
}

// The `derive` attribute automatically creates the implementation
// required to make this `struct` printable with `fmt::Debug`.
#[derive(Drop, Debug)]
struct DebugPrintable {
    value: felt252,
}

// Derive the `fmt::Debug` implementation for `Structure`.
#[derive(Drop, Debug)]
struct Structure {
    value: felt252,
}

// Put a `Structure` inside of the structure `Deep`. Make it printable
// also.
#[derive(Drop, Debug)]
struct Deep {
    inner: Structure,
}

fn main() {
    // Printing with `{:?}` is similar to with `{}`.
    println!("{:?} months in a year.", 12);
    let christian: ByteArray = "Christian";
    let slater: ByteArray = "Slater";
    let object: ByteArray = "actor's";
    println!("{1:?} {0:?} is the {2:?} name.", slater, christian, object);

    // `Structure` is printable!
    println!("Now {:?} will print!", Structure { value: 3 });

    // The problem with `derive` is there is no control over how
    // the results look. What if I want this to just show a `7`?
    println!("Now {:?} will print!", Deep { inner: Structure { value: 7 } });
}
