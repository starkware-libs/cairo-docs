# Debug

This is the Cairo adaptation of [Rust By Example's _Debug_ chapter](https://doc.rust-lang.org/rust-by-example/print_debug.html):

```cairo,editable
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
```

### Activities

- Try removing the `Debug` derive from one of the structs and see what error you get
- Add a new field to the `Person` struct and see how it appears in the debug output
- Try implementing `Display` for one of the structs to control its output format

### See also:

[`derive`][derive], [`core::fmt`][fmt], and [`struct`][structs]

[derive]: ../../trait/derive.md
[fmt]: https://docs.swmansion.com/scarb/corelib/core-fmt.html
[structs]: ../../custom_types/structs.md
