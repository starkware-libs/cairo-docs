//TAG: does_not_run

struct Structure {
    inner: i32,
}

fn main() {
    // In general, the `{}` will be automatically replaced with any
    // arguments. These will be stringified.
    println!("{} days", 31);

    // Positional arguments can be used. Specifying an integer inside `{}`
    // determines which additional argument will be replaced. Arguments start
    // at 0 immediately after the format string.
    let alice: ByteArray = "Alice";
    let bob: ByteArray = "Bob";
    println!("{0}, this is {1}. {1}, this is {0}", alice, bob);

    // Different formatting can be invoked by specifying the format character
    // after a `:`.
    println!("Base 10:               {}", 69420); // 69420
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c

    // Cairo even checks to make sure the correct number of arguments are used.
    let bond: ByteArray = "Bond";
    println!("My name is {0}, {1} {0}", bond);
    // FIXME ^ Add the missing argument: "James"

    // Only types that implement fmt::Display can be formatted with `{}`. User-
// defined types do not implement fmt::Display by default.

    // This will not compile because `Structure` does not implement
// fmt::Display.
// println!("This struct `{}` won't print...", Structure(3));
// TODO ^ Try uncommenting this line
}
